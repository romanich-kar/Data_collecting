# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import TakeFirst, MapCompose


def get_link(values):
    pattern = re.compile('<\d+ (.+)>')
    values = re.findall(pattern, values)
    return values


def edit_definitions(values):
    pattern = re.compile('\\n +')
    values = re.sub(pattern, '', values)
    try:
        return int(values)
    except ValueError:
        return values


def change_price(values):
    values = int(values)
    return values


class LM_Item(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose())
    terms = scrapy.Field(input_processor=MapCompose())
    definitions = scrapy.Field(input_processor=MapCompose(edit_definitions))
    price = scrapy.Field(input_processor=MapCompose(change_price))
    characteristic = scrapy.Field()
    link = scrapy.Field(output_processor=MapCompose(get_link))