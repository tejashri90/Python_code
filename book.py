import scrapy

class Book(scrapy.Spider):
    name = 'book'
    start_urls = [
        'http://books.toscrape.com/'
    ]

    def parse(self, response):
        for link in response.xpath('//article[@class="product_pod"]/div/a/@href').extract():
            yield response.follow(link, callback=self.parse_detail)
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_detail(self, response):
        book_title = response.xpath('//div[contains(@class, "product_main")]/h1/text()').extract_first()
        book_price = response.xpath('//div[contains(@class, "product_main")]/'
                               'p[@class="price_color"]/text()').extract_first()
							   
        image_url = response.xpath('//div[contains(@class, "item active")]/img/@src').extract_first()
		
	#detai = response.xpath('//div[contains(@class, "image_container")]/p/a/@href').extract_first()
	detail_page_url = response.xpath('//article[@class="product_pod"]/div/a/@href').extract_first()
        
        yield {
            'book_title': book_title,
            'book_price': book_price,
            'image_url': image_url,
			'detail_page_url': detail_page_url
            
        }