# useful for handling different item types with a single interface
# from scrapy.pipelines.images import ImagesPipeline

class BurberryNewPipeline():
    def process_item(self, item, spider):
        return item
