
import scrapy


class WhiskeySpider(scrapy.Spider):
    name = "whisky"
    start_urls = [
        'https://www.celticwhiskeyshop.com/scottish-whisky-home-page']

    def parse(self, response):
        for products in response.css('div.product-details'):
            try:
                yield{
                    'product': products.css('a::text').get(), # products.xpath('//*[@id="content"]/div[4]/div[1]/div/div[2]/div[1]/h4/a/text()').get(),
                    'price': products.css('p.price::text').get().replace('€', "").strip(),
                    'link': products.css('a').attrib['href'], # products.xpath('//*[@id="content"]/div[4]/div[1]/div/div[2]/div[1]/h4/a/@href').get(),
                    }
            except:
                 yield{
                    'product': 'a',
                    'price': 'a',
                    'link': 'a',
                    }
         
        next_page = response.xpath('//*[@id="content"]/div[5]/div[1]/ul/li[10]/a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

# https://www.youtube.com/watch?v=s4jtkzHhLzY&t=573s

