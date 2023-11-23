import scrapy
import re

class PokeSpiderSpider(scrapy.Spider):
    name = 'poke_spider'
    allowed_domains = ['scrapeme.live']
    start_urls = ['https://scrapeme.live/shop/page/1']

    def parse(self, response):
        product_links = response.xpath('//ul[contains(@class, "products")]/li/a[1]/@href').getall()
        for link in product_links:
            yield response.follow(url=link, callback=self.parse_page)

        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_page(self, response):
        dimensions = response.css('.product_dimensions::text').get()
        height, length, width = None, None, None

        if dimensions:
            match = re.match(r'(\d+)\s*x\s*(\d+)\s*x\s*(\d+)', dimensions)

            if match:
                height, length, width = match.groups()

        yield {'name' : response.css('h1.product_title::text').get(),
        'price' : response.css('.price span.woocommerce-Price-amount.amount::text').get(),
        'description' : response.css('div.woocommerce-Tabs-panel p::text').get(),
        'stock' : response.css('.stock::text').get(),
        'sku' : response.css('.sku::text').get(),
        'categories' : response.css('.posted_in a::text').getall(),
        'tags' : response.css('.tagged_as a::text').getall(),
        'weight' : response.css('.product_weight::text').get(),
        'height' : height,
        'length' : length,
        'width' : width
        
}




        # stock = response.css('.stock::text').get()
        # stock_divise = stock.split(" ")[0]

        # weight = response.css('.product_weight::text').get()
        # weight_divise = weight.split(" ")[0]


        # dimensions = response.css('.product_dimensions::text').get()
        # dimensions_divisées = dimensions.split(" ")
        # height = dimensions_divisées[0]
        # length = dimensions_divisées[2]
        # width = dimensions_divisées[4]

        
        # yield {'name' : response.css('h1.product_title::text').get(),
        # 'price' : response.css('.price span.woocommerce-Price-amount.amount::text').get(),
        # 'description' : response.css('div.woocommerce-Tabs-panel p::text').get(),
        # 'stock' : stock_divise,
        # 'sku' : response.css('.sku::text').get(),
        # 'categories' : response.css('.posted_in a::text').getall(),
        # 'tags' : response.css('.tagged_as a::text').getall(),
        # 'weight' : weight_divise,
        # 'height' : height,
        # 'length' : length,
        # 'width' : width}

        

        # poke_scrap_item = PokeScrapItem()


        # poke_scrap_item['name'] = response.css('h1.product_title::text').get(),
        # poke_scrap_item['price'] = response.css('.price span.woocommerce-Price-amount.amount::text').get(),
        # poke_scrap_item['description'] = response.css('div.woocommerce-Tabs-panel p::text').get(),
        # poke_scrap_item['stock'] = stock_divise,
        # poke_scrap_item['sku'] = response.css('.sku::text').get(),
        # poke_scrap_item['categories'] = response.css('.posted_in a::text').getall(),
        # poke_scrap_item['tags'] = response.css('.tagged_as a::text').getall(),
        # poke_scrap_item['weight'] = weight_divise,
        # poke_scrap_item['height'] = height,
        # poke_scrap_item['length'] = length,
        # poke_scrap_item['width'] = width

        # yield poke_scrap_item
