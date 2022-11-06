import scrapy
from scrapy_playwright.page import PageMethod



class TomatoReviewSpider(scrapy.Spider):
    name = 'tomato_review'
   
    def start_requests(self):
        links = ['https://www.rottentomatoes.com/m/captain_america_the_first_avenger/reviews',
                 'https://www.rottentomatoes.com/m/captain_america_the_first_avenger/reviews?type=top_critics',
                ]
        
        for url in links:
            yield scrapy.Request(
                                url, 
                                meta = dict(
                                playwright =  True,
                                playwright_include_page = True,
                                playwright_page_methods = [PageMethod("wait_for_selector", "div.review_table")])
                                )



    def parse(self, response):
        
        pass
