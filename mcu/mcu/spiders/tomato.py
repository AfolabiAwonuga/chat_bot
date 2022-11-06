import scrapy
from scrapy_playwright.page import PageMethod

class TomatoSpider(scrapy.Spider):
    name = 'tomato'
   

    def start_requests(self):
        yield scrapy.Request(
                            'https://www.rottentomatoes.com/m/captain_america_the_first_avenger', 
                            meta = dict(
                            playwright =  True,
                            playwright_include_page = True,
                            playwright_page_methods = [PageMethod("wait_for_selector", "div.centered")])
                            )
    
    def parse(self, response):
        pass
