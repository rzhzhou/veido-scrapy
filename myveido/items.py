# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VeidoDetailsItem(scrapy.Item):
    url = scrapy.Field()
    thumb = scrapy.Field()
    score = scrapy.Field()
    title = scrapy.Field()
    introduction = scrapy.Field()
    director = scrapy.Field()
    star = scrapy.Field()
    videotype = scrapy.Field()
    status = scrapy.Field()
    is_new = scrapy.Field()


class VideoContent(scrapy.Item):
    name = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    videodetails_id = scrapy.Field()

