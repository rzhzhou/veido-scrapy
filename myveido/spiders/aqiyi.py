import scrapy
from sqlalchemy.orm import sessionmaker
from scrapy_splash import SplashRequest
from myveido.models import (db_dyy, Category, VideoType, Star, Director,
                             VideoDetails, VideoContent, VideodetailsVideotype, VideodetailsStar)


class AqiyiSpider(scrapy.Spider):
    name = 'aqiyi'
    allowed_domains = ['so.iqiyi.com']
    start_urls = ['https://so.iqiyi.com']


    def linkDb(self, dataBase):
        db = dataBase
        Session = sessionmaker(bind=db)
        session = Session()

        return session

    def parse(self, response):
        video_name = self.acquire_name()
        for index in range(len(video_name)):
            # print(video_name[index]['id'],video_name[index]['title'])
            url = 'https://so.iqiyi.com/so/q_' + video_name[index]['title']
            yield scrapy.Request(url, callback=self.parse_item)


    def acquire_name(self):
        VideoName = []
        session = self.linkDb(db_dyy())
        details = session.query(VideoDetails).filter(VideoDetails.status == 1).all()
        for index in details:
            videodict = {}
            videodict = {
                'id' : index.id,
                'title' : index.title,
            }
            VideoName.append(videodict)
        # print(VideoName)
        return VideoName

    def parse_item(self, response):
        # url = response.xpath('//div[@desc="搜索列表"]/div[1]/div/div[2]/div[2]')
        url = response.css('.result-bottom>.result-bottom-pos').extract()
        # director = response.xpath('//div[@desc="搜索列表"]//div[1]/div/div[2]/div[1]/div[1]/a/text()').extract()
        print(url)