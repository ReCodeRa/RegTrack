# Derived from scrapy tutorial

import scrapy

# Spider arguments are passed in the crawl command using the -a option. For example:

# scrapy crawl myspider -a category=electronics -a domain=system
# Spiders can access arguments as attributes:

# class MySpider(scrapy.Spider):
#     name = 'myspider'

#     def __init__(self, category='', **kwargs):
#         self.start_urls = [f'http://www.example.com/{category}']  # py36
#         super().__init__(**kwargs)  # python3

#     def parse(self, response)
#         self.log(self.domain)  # system
# 'Taken from the Scrapy doc: http://doc.scrapy.org/en/latest/topics/spiders.html#spider-arguments'

class suklSpider(scrapy.Spider):
    name = "sukl"
    # Pagination 50
    start_urls = ["""https://www.sukl.cz/modules/medication/search.php?data%5Bsearch_for%5D=&data%5Bcode%5D=&data%5Batc_group%5D=&data%5Bmaterial%5D=loperamide&data%5Bpath%5D=&data%5Breg%5D=&data%5Bradio%5D=none&data%5Brc%5D=&data%5Bchbox%5D%5B%5D=braill-yes&data%5Bchbox%5D%5B%5D=braill-no&data%5Bchbox%5D%5B%5D=braill-def&data%5Bwith_adv%5D=0&search=Vyhledat&data%5Blisting%5D=50"""]
    
    # Pagination 100
    # start_urls = ["""https://www.sukl.cz/modules/medication/search.php?data%5Bsearch_for%5D=&data%5Bcode%5D=&data%5Batc_group%5D=&data%5Bmaterial%5D=loperamide&data%5Bpath%5D=&data%5Breg%5D=&data%5Bradio%5D=none&data%5Brc%5D=&data%5Bchbox%5D%5B%5D=braill-yes&data%5Bchbox%5D%5B%5D=braill-no&data%5Bchbox%5D%5B%5D=braill-def&data%5Bwith_adv%5D=0&search=Vyhledat&data%5Blisting%5D=100"""]
    # URL cannot be parsed properly
        
    def parse(self, response): 
        for product in response.css('tr.first'):
            yield {
                   'brand_pcg' : product.css('td  a::attr(title)').get(), #N36
                   'detail': product.css('td a::attr(href)').get() #N61
            } 
           
        next_page = response.css('p.pager a.nav::attr(href)').get()  
        if next_page is not None:
           next_page_url = 'https://www.sukl.cz/' + next_page
           yield response.follow(next_page_url, callback=self.parse)

