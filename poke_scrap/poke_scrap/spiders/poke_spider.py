import scrapy

class PokeSpiderSpider(scrapy.Spider):
    name = 'poke_spider'
    allowed_domains = ['scrapeme.live']
    start_urls = ['https://scrapeme.live/shop/page/1']

    def parse(self, response):
    # Extraire les liens des pages de produits
        product_links = response.xpath('//ul[contains(@class, "products")]/li/a[1]/@href').getall()
        for link in product_links:
            yield response.follow(url=link, callback=self.parse_page)

        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_page(self, response):
        # Extraire les données des pages de produits
        yield {'name' : response.css('h1.product_title::text').get(),
        'price' : response.css('.price span.woocommerce-Price-amount.amount::text').get(),
        'description' : response.css('div.woocommerce-Tabs-panel p::text').get(),
        'stock' : response.css(' .stock::text').get(),
        'sku' : response.css('.sku::text').get(),
        'categories' : response.css('.posted_in a::text').getall(),
        'tags' : response.css('.tagged_as a::text').getall(),
        'weight' : response.css('.product_weight::text').get(),
        'dimensions' : response.css('.product_dimensions::text').get()}
