import json
import requests
import scrapy
import response
import html5lib
from cssselect import Selector
import csv

from scrapy import Request

from ..items import DatabaseTestItem


class MedicineSpider(scrapy.Spider) :
    name = 'medicine_spider'
    start_urls = ["https://www.justdial.com/Delhi/Gyms/nct-11575244-1"]

    def start_requests(self) :
        headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls :
            yield Request(url, headers=headers)

    def parse(self, response) :
        items = DatabaseTestItem()
        product_name = response.css('.contact-info').extract()
        items['product_name'] = product_name
        yield items
        pass
