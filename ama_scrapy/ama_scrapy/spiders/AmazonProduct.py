import scrapy
from ..items import 

class AmazonproductSpider(scrapy.Spider):
    name = 'AmazonProduct'
    allowed_domains = ['amazon.co.jp']
    start_urls = ['http://amazon.co.jp/']

    #クロールを開始するURLを動的に変えたい
    def start_request(self):
        for url in self.urls:
        url = 'https://sardine-system.com/media/'
        yield scrapy.Request(url, callback=self.parse)
    
    def parse(self, response):
        """
        レスポンスに対するパース処理
        """
        for post in response.css():
            yield  Post(
                name=post.css("span.a-profile-name::text").get(),
                title = post.css(".review-title>span::text").get(),
            )
    # 再帰的にページングを辿るための処理
        older_post_link = response.css('.blog-pagination a.next-posts-link::attr(href)').extract_first()
        if older_post_link is None:
     # リンクが取得できなかった場合は最後のページなので処理を終了
            return
     # URLが相対パスだった場合に絶対パスに変換する
        older_post_link = response.urljoin(older_post_link)
        # 次のページをのリクエストを実行する
        yield scrapy.Request(older_post_link, callback=self.parse)

#https://qiita.com/Chanmoro/items/f4df85eb73b18d902739