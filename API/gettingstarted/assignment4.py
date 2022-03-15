import pandas
import numpy
from scipy import special
import scrapy

arr1 = [1,2,3,4,5]
test1 = pandas.Series(arr1, name="Test Print")
print(test1)

names = ["Peter", "Paul", "Tracy", "Trucy"]
years = [3, 2, 4, 1]
majors = ["Computer Science", "Computer Information System", "Computer Engineering", "Undeclared"]
test2 = pandas.DataFrame({
    "Name" : names,
    "Year" : years,
    "Major" : majors
})
print(test2)

print("\nThis is a test of Numpy! \n")
a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
b = numpy.array([2,2,2])
c = a * b #element wise multiplication
print(c)
print("")
c = b @ a #matrix multiplication
print(c)

print("\nPermutation example: 7 and 3")
d = special.perm(7, 3, exact = True)
print(d)

class MySpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https:quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']").extract()
        yield{'quotes': quotes}
print(quotes)

                                
