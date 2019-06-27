import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'shahryar'
    start_urls = [
        'https://ganjoor.net/shahriar/gozidegh/sh'+str(num)+'/' for num in range(1, 161)
    ]

    def parse(self, response):
        mesras = []
        for mesra in response.xpath('//div[@class="b"]//text()').extract():
            if mesra.strip() != "":
                mesras.append(mesra)
        yield {
            'ghazal': mesras
        }
