import scrapy
import requests
from lxml import html
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client.books

class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['https://www.labirint.ru']
    start_urls = ['http://https://www.labirint.ru/books/']
    response = requests.get('http://https://www.labirint.ru/books/')
    root = html.fromstring(response.text)
    a = root.xpath('//*[@id="catalog-navigation"]/form/div[1]/div[2]/div/div/span[1]/span/text()')
    pages_count = int(input('Всего на сайте ', a, ' книг. Информацию о скольких хотите собрать? '))

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'https://www.labirint.ru/books/{page}/'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = {
            'url': response.request.url,
            'title': response.css('#product-title::text').extract_first().strip(),
            'author': response.css('div.authors a::text').extract_first().strip(),
            'price': response.css('span.buying-priceold-val-number::text').extract_first().strip(),
            'discount_price': response.css('span.buying-pricenew-val-number::text').extract_first().strip(),
            'rating': response.css('#rate::text').extract_first().strip()
        }

        db.labirint.insert(item)
        yield item
