# import scrapy

# class PokeSpiderSpider(scrapy.Spider):
#     name = 'poke_spider'
#     allowed_domains = ['scrapeme.live']
#     start_urls = ['http://scrapeme.live/']

#     def parse(self, response):
#         links = response.css('ul.products.columns-4 > li > a::attr(href)').getall()

#         for link in links:
#             yield scrapy.Request(url=link, callback=self.parse_page)

#     def parse_page(self, response):
#         name = response.css('div.summary entry-summary h1::text').get()
#         price = response.css('div.summary entry-summary .price::text').get()
#         description = response.css('div.woocommerce-tabs wc-tabs-wrapper .woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab p::text').get()
#         stock = response.css('div.summary entry-summary .stock::text').get()
       
#         sku = response.css('div.summary entry-summary div.product_meta  .sku_wrapper .sku::text').get()
#         categories = response.css('div.summary entry-summary .posted_in a::text').get()
#         tags = response.css('div.summary entry-summary tagged_as a::text').get()

#         weight = response.css('div.woocommerce-Tabs-panel woocommerce-Tabs-panel--additional_information panel entry-content wc-tab .shop_attributes tr product_weight::text').get()
#         dimensions = response.css().get('div.woocommerce-Tabs-panel woocommerce-Tabs-panel--additional_information panel entry-content wc-tab .shop_attributes tr product_dimensions::text')

#         yield {
#             'name': name,
#             'price': price,
#             'description': description,
#             'stock': stock,
#             'tags': tags,
#             'categories': categories,
#             'sku': sku,
#             'weight': weight,
#             'dimensions': dimensions
#         }


# -----------------------------------------
# -----------------------------------------

import scrapy

class PokeSpiderSpider(scrapy.Spider):
    name = 'poke_spider'
    allowed_domains = ['scrapeme.live']
    start_urls = ['http://scrapeme.live/']

    def parse(self, response):
        links = response.css('ul.products.columns-4 > li > a::attr(href)').getall()

        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_page)

    def parse_page(self, response):
        name = response.css('div.summary.entry-summary h1::text').get()
        price = response.css('div.summary.entry-summary .price::text').get()
        description = response.css('div.woocommerce-tabs.wc-tabs-wrapper .woocommerce-Tabs-panel.woocommerce-Tabs-panel--description.panel.entry-content.wc-tab p::text').get()
        stock = response.css('div.summary.entry-summary .stock::text').get()
       
        sku = response.css('div.summary.entry-summary div.product_meta .sku_wrapper .sku::text').get()
        categories = response.css('div.summary.entry-summary .posted_in a::text').get()
        tags = response.css('div.summary.entry-summary.tagged_as a::text').get()

        weight = response.css('div.woocommerce-Tabs-panel.woocommerce-Tabs-panel--additional_information.panel.entry-content.wc-tab .shop_attributes tr.product_weight td::text').get()
        dimensions = response.css('div.woocommerce-Tabs-panel.woocommerce-Tabs-panel--additional_information.panel.entry-content.wc-tab .shop_attributes tr.product_dimensions td::text').get()

        yield {
            'name': name,
            'price': price,
            'description': description,
            'stock': stock,
            'tags': tags,
            'categories': categories,
            'sku': sku,
            'weight': weight,
            'dimensions': dimensions
        }
