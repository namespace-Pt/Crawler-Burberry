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
            # 'https://cn.burberry.com/mens-new-arrivals-new-in/'
            "https://cn.burberry.com/service/shelf/mens-new-arrivals-new-in/"
        ]
        for url in urls:
            url = url + '?_=' + str(round(time.time()*1000))
            yield scrapy.Request(url=url, callback=self.parse, headers=HEADER)

    def parse_product(self, response):
        """
            parse the product page, download the first image
        """
        product = BurberryNewItem()
        product['image_urls'] = [urljoin('https:',response.xpath("//div[@class='product-carousel_item']/picture//img/@data-src").get())]
        product['price'] = response.xpath("//span[@class='product-purchase_price']/text()").get()
        product['name'] = response.xpath("//h1[@class='product-purchase_name']/text()").get()
        return product

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
            read the main page, get entries to every new products
        """
        # products_url = response.xpath("//div[@class='product_container']/a/@href").getall()
        # for product in products_url:
        #     yield scrapy.Request(url=response.urljoin(product), callback=self.parse_product)
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