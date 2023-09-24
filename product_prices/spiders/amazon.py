import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://amazon.com/s?k=raspberry"]

    def parse(self, response):
        for product in response.css('div.s-include-content-margin'):
            yield {
                
                    'product_name': product.css('span.a-size-medium::text').get(),
                    'price': product.css('span.a-price span.a-price-whole::text').get(),
            }
        next_page = response.css('li.a-last a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
