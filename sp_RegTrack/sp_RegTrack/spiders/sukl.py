# Derived from scrapy tutorial

import scrapy

class suklSpider(scrapy.Spider):
    name = "sukl"

    start_urls = ["""https://www.sukl.cz/modules/medication/search.php?data%5Bsearch_for%5D=&data%5Bcode%5D=&data%5Batc_group%5D=&data%5Bmaterial%5D=loperamide&data%5Bpath%5D=&data%5Breg%5D=&data%5Bradio%5D=none&data%5Brc%5D=&data%5Bchbox%5D%5B%5D=braill-yes&data%5Bchbox%5D%5B%5D=braill-no&data%5Bchbox%5D%5B%5D=braill-def&data%5Bwith_adv%5D=0&search=Vyhledat&data%5Blisting%5D=100"""]
    # URL cannot be parsed properly
        
    def parse(self, response): 
        for product in response.css('tr.first'):
            yield {
                   'brand_pcg' : product.css('td  a::attr(title)').get() 
                   'spc': product.css('td:nth-child(3) a::attr(href)').get()
                   'detail': product.css('td a::attr(href)').get()
            } 
           
           
        next_page = response.css()
