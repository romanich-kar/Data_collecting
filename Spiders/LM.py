import scrapy
from scrapy.http import HtmlResponse
from leroy.items import LM_Item
from scrapy.loader import ItemLoader

text = 'обои'
class LMSpider(scrapy.Spider):
    name = 'LM'
    allowed_domains = ['leroymerlin.ru']
    q = input('Введите запрос: ')
    start_urls = [f'https://leroymerlin.ru/search/?q={q}']

    def parse(self, response: HtmlResponse):
        product_links = response.xpath("//div[@class='hover-image-buttons']/a/@href").extract()
        for link in product_links:
            if 'product' in link:
                yield response.follow(link, callback=self.parse_product)

        next_page = response.xpath("//div[@class='next-paginator-button-wrapper']/a/@href").extract_first()
        yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response: HtmlResponse):
        loader = ItemLoader(item=LM_Item(), response=response)

        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('photos', "//source[@media=' only screen and (min-width: 1024px)']/@srcset")
        loader.add_xpath('terms', "//dt/text()")
        loader.add_xpath('definitions', "//dd/text()")
        loader.add_xpath('price', "//meta[@itemprop='price']/@content")
        loader.add_value('link', str(response))

        yield loader.load_item()