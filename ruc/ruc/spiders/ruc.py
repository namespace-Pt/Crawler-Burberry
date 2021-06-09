import scrapy
from ..settings import HEADER
from ..passward import ID,PSWD

class RUCSpider(scrapy.Spider):
    name = "ruc"

    def start_requests(self):
        urls = [
            # important to use this url
            "https://v.ruc.edu.cn/auth/login?&proxy=true&redirect_uri=https%3A%2F%2Fv.ruc.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3Daccounts.tiup.cn%26redirect_uri%3Dhttps%253A%252F%252Fv.ruc.edu.cn%252Fsso%252Fcallback%253Fschool_code%253Druc%2526theme%253Dschools%26response_type%3Dcode%26school_code%3Druc%26scope%3Dall%26state%3DngxKxdklsXZvSl3U%26theme%3Dschools&school_code=ruc"
        ]

        formdata = {
            "username":"ruc:" + ID,
            "password":PSWD,
        }

        for url in urls:
            # append timestamp
            # set headers
            yield scrapy.FormRequest(url=url, callback=self.parse, headers=HEADER, formdata=formdata)

    def parse(self, response):
        print(response.content)