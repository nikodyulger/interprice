from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os 

process = CrawlerProcess(get_project_settings())
process.crawl(os.environ['SPIDER_NAME'], n_pages=os.environ['N_PAGES'])
process.start()