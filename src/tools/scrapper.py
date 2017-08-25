import scrapy

# 'http://quotes.toscrape.com/tag/humor/',

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.nba.com/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
