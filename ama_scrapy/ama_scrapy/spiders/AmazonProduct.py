import scrapy


class AmazonproductSpider(scrapy.Spider):
    name = 'AmazonProduct'
    allowed_domains = ['amazon.co.jp']
    start_urls = ['http://amazon.co.jp/']

    def parse(self, response):
        pass


#https://qiita.com/Chanmoro/items/f4df85eb73b18d902739