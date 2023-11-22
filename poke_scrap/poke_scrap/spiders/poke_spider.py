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

# import scrapy
# import csv

# class PokeSpiderSpider(scrapy.Spider):
#     name = 'poke_spider'
#     allowed_domains = ['scrapeme.live']
#     start_urls = ['http://scrapeme.live/']

#     def parse(self, response):
#         links = response.css('ul.products.columns-4 > li > a::attr(href)').getall()

#         for link in links:
#             yield scrapy.Request(url=link, callback=self.parse_page)

#     def parse_page(self, response):
#         name = response.css('div.summary.entry-summary h1::text').get()
#         price = response.css('div.summary.entry-summary .price::text').get()
#         description = response.css('div.woocommerce-tabs.wc-tabs-wrapper .woocommerce-Tabs-panel.woocommerce-Tabs-panel--description.panel.entry-content.wc-tab p::text').get()
#         stock = response.css('div.summary.entry-summary .stock::text').get()
       
#         sku = response.css('div.summary.entry-summary div.product_meta .sku_wrapper .sku::text').get()
#         categories = response.css('div.summary.entry-summary .posted_in a::text').get()
#         tags = response.css('div.summary.entry-summary.tagged_as a::text').get()

#         weight = response.css('div.woocommerce-Tabs-panel.woocommerce-Tabs-panel--additional_information.panel.entry-content.wc-tab .shop_attributes tr.product_weight td::text').get()
#         dimensions = response.css('div.woocommerce-Tabs-panel.woocommerce-Tabs-panel--additional_information.panel.entry-content.wc-tab .shop_attributes tr.product_dimensions td::text').get()

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

#         with open('output.json', 'a', encoding='utf-8') as f:
#             json.dump(item, f, ensure_ascii=False, indent=2)

#         # Renvoyer les données pour le pipeline ou d'autres traitements
#         yield item


# -----------------------------------------
# ---------------------------------------------

# import scrapy

# class PokeSpiderSpider(scrapy.Spider):
#     name = 'poke_spider'
#     allowed_domains = ['scrapeme.live']
#     start_urls = ['http://scrapeme.live/shop/']

#     def parse(self, response):
#     # Extraire les liens des pages de produits
#         product_links = response.css('ul.products.columns-4 > li > a::attr(href)').getall()

#     # Suivre chaque lien de produit
#         for link in product_links:
#             yield scrapy.Request(url=response.urljoin(link), callback=self.parse_page)


#     def parse_page(self, response):
#         # Extraire les données des pages de produits
#         yield {'name' : response.css('div.summary entry-summary h1::text').get(),
#         'price' : response.css('div.summary entry-summary .price::text').get(),
#         'description' : response.css('div.woocommerce-tabs wc-tabs-wrapper .woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab p::text').get(),
#         'stock' : response.css('div.summary entry-summary .stock::text').get(),
#         'sku' : response.css('div.summary entry-summary div.product_meta  .sku_wrapper .sku::text').get(),
#         'categories' : response.css('div.summary entry-summary .posted_in a::text').get(),
#         'tags' : response.css('div.summary entry-summary tagged_as a::text').get(),
#         'weight' : response.css('div.woocommerce-Tabs-panel woocommerce-Tabs-panel--additional_information panel entry-content wc-tab .shop_attributes tr product_weight::text').get(),
#         'dimensions' : response.css('div.woocommerce-Tabs-panel.woocommerce-Tabs-panel--additional_information.panel.entry-content.wc-tab .shop_attributes tr.product_dimensions::text').get()}


import scrapy

class PokeSpiderSpider(scrapy.Spider):
    name = 'poke_spider'
    allowed_domains = ['scrapeme.live']
    start_urls = ['https://scrapeme.live/shop/page/1']

    # def parse(self, response):
    # # Extraire les liens des pages de produits
    #     next_links = response.css('a.next.page-numbers::attr(href)').get()

    #     for next_link in next_links:
    #         yield response.follow(url=next_link, callback=self.parse2)

    def parse(self, response):
        # Extraire le lien de la page suivante
        next_link = response.css('').get()

        # Suivre le lien de la page suivante
        if next_link:
            yield response.follow(url=next_link, callback=self.parse2)


    def parse2(self, response):
    # Extraire les liens des pages de produits
        product_links = response.xpath('//ul[contains(@class, "products")]/li/a[1]/@href').getall()
        # product_links = response.css('ul.products.columns-4 li a::attr(href)').getall()

    # Suivre chaque lien de produit
        for link in product_links:
            yield response.follow(url=link, callback=self.parse_page)


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

       


