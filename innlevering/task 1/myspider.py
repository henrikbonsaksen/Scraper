import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from vergeSpider.items import VergeReview


class ArticleSpider(CrawlSpider):
    name = 'articles'

    allowed_domains = ['www.theverge.com']
    start_urls = ['https://www.theverge.com/reviews']

    rules = [
        Rule(LinkExtractor(allow=r'^(https://www.theverge.com/)(\d+/)([^/]*)$'),
             callback='parse_items', follow=True, cb_kwargs={'match': True}),

    ]

    def parse_items(self, response, match):
        print(response.url)
        title = response.css('h1::text').extract_first()
        author = response.selector.xpath('//*[@class="c-byline__author-name"]/text()').get()
        author_url = response.selector.xpath('//*[@class="c-byline__item"]/a/@href').extract_first()

        if match:
            url = response.url
            review = VergeReview()
            review['url'] = url
            review['title'] = title
            review['author'] = author
            review['authorURL'] = author_url
            print(review)
        else:
            url = response.url
            print('No match: {}'.format(url))

        return review


"""
scrapy runspider spiders/myspider.py -o article.csv csv -s CLOSESPIDER_PAGECOUNT=20
"""
