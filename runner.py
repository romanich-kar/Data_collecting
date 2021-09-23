from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from leroy import settings
from leroy.spiders.LM import LM

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LM)
    process.start()