import re

import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        table = response.css(
            'section[id="numerical-index"]').css('tbody')
        links = table.css('a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pattern = r'^PEP\s(?P<number>\d+)\s[–]+\s(?P<name>.*)'
        table = response.css('section[id="pep-content"]')
        pep = table.css('h1.page-title::text').get()
        text_match = re.search(pattern, pep)
        pep_number, pep_name = text_match.groups()
        pep_status = table.css('dt:contains("Status") + dd::text').get()
        yield {
            'number': pep_number,
            'name': pep_name,
            'status': pep_status
        }
