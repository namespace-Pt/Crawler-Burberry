from urllib.parse import urljoin
import scrapy
import json
import time
from ..settings import HEADER, IMAGES_STORE
from ..items import BurberryNewItem

class BurberrySpider(scrapy.Spider):
    name = "burberry"

    def start_requests(self):
        urls = [
            # important to use this url
            "https://cn.burberry.com/service/shelf/mens-new-arrivals-new-in/"
        ]
        for url in urls:
            # append timestamp
            url = url + '?_=' + str(round(time.time()*1000))

            # set headers
            yield scrapy.Request(url=url, callback=self.parse, headers=HEADER)

    def download(self, response):
        """
            download image from the url.
            comment:
                I tried to extend the default ImagePipeline, but I have to say it's bullshit.
                I write the download function here to get rid of pipelines, which is not the
                main point of this project.
        """
        item = response.meta['item']
        with open(IMAGES_STORE + item['name'] + '-' + item['price'] + '.jpg', 'wb') as f:
            f.write(response.body)

        yield item

    def parse(self, response):
        """
            parse the json response
        """
        products = json.loads(response.text)
        for product in products:
            item = BurberryNewItem()
            try:
                item['name'] = product['label']
                item['price'] = str(product['price'])
                image_url = urljoin('https:',product['images']['sources'][0]['srcset'].split(',')[0])
                yield scrapy.Request(image_url, meta={'item':item}, callback=self.download)

            except:
                print(product)