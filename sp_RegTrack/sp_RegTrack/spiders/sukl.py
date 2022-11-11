# Derived from scrapy tutorial

import scrapy

class suklSpider(scrapy.Spider):
    name = "sukl"

    def start_requests(self):
        urls = [
            "https://www.sukl.cz/modules/medication/search.php?data%5Bsearch_for%5D=&data%5Bcode%5D=&data%5Batc_group%5D=B01AF03&data%5Bmaterial%5D=&data%5Bpath%5D=&data%5Breg%5D=&data%5Bradio%5D=none&data%5Brc%5D=&data%5Bchbox%5D%5B%5D=braill-yes&data%5Bchbox%5D%5B%5D=braill-no&data%5Bchbox%5D%5B%5D=braill-def&data%5Bwith_adv%5D=0&search=Vyhledat&data%5Blisting%5D=100"
        ]
        
    
    def parse(self, response): 
        recs = []
        for product in response.css('tr.first'):
            r = yield {
                   'brand':product.css('[td.headers="název"]::text').get() 
            }
            recs.append(r) 
           
           
 #           next_page = response.css()