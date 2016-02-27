# -*- coding: utf-8 -*-
# just for user agent testing purposes

import scrapy
import logging
from bs4 import BeautifulSoup

class UATesterSpider(scrapy.Spider):
    name = 'UAtester'
    allowed_domains = ['whatsmyuseragent.com']
    start_urls = (
        'http://whatsmyuseragent.com',
    )

    def parse(self, response):
    	soup = BeautifulSoup(response.body, 'html.parser')
        ua = soup.select('h2.info')[0].encode('UTF-8').get_text()
        logging.info("USER AGENT = %s" % ua)
        pass