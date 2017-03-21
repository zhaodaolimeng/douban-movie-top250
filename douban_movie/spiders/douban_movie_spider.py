import scrapy
import re

class DoubanMovieSpider(scrapy.Spider):
    name = "douban_movie"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "https://movie.douban.com/top250"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        for item in response.css('div.info'):
            names = item.css('span.title::text')
            name_cn = names[0].extract()
            name_en = names[1].extract() if len(names) == 2 else ''

            film_info = item.xpath('div[contains(@class, "bd")]/p/text()').extract()
            # director = director_actor.split('\xa0\xa0\xa0')[0].split(':')[1]
            # actor = director_actor.split('\xa0\xa0\xa0')[1].split(': ')[1]
            year_country_type = film_info[1]
            year = re.findall('\d+', year_country_type)
            country = year_country_type.split('\xa0/\xa0')[1]
            types = year_country_type.split('\xa0/\xa0')[2].split('\n', 1)[0]

            yield {
                'name_cn': name_cn,
                'name_en': name_en,
                'name_other': item.css('span.other::text').extract_first(),
                'director_actor': film_info[0],
                'year': year,
                'country': country,
                'types': types,
                'comment': item.css('span.inq::text').extract_first()
            }

            next_page = response.css('span.next a::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
