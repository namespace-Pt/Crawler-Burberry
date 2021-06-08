# useful for handling different item types with a single interface
import logging
from .settings import IMAGES_STORE
# from scrapy.pipelines.images import ImagesPipeline

class BurberryNewPipeline():
    def process_item(self, item, spider):
        return item
