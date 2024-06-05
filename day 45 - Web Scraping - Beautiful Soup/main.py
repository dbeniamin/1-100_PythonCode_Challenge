# ## documentation for beautiful soup
# ## https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests

# # add encoding type otherwise if you get an error when opening with python
# # obtain the encoding from the html file <meta charset="utf-8">
# with open("website.html", encoding='UTF8') as file:
#     contents = file.read()
#
# # pass the content as text and the parser
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # can print soup.prettify() =  the indented code
#
# all_anchor = soup.find_all(name="a")  # will find all anchor tags, can be used for all typs of tags
#
# for tag in all_anchor:
#     print(tag.getText())  # use .getText() to extract the text of the tags
#     print(tag.get("href"))  # use .get("attribute name") to extract the specific attribute
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# # class is a reserved notation in Python
# # class_ has to be used to avoid errors when passing a class filtering / finding action
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# # can use selectors to find specific items
# # select_one() => will find the first matching selector
# # select() => will find all the matching selectors
# company_url = soup.select_one(selector="p a")  # i.e find an a tag that is inside a p tag
# print(company_url)
#
# # using id selectors
# name = soup.select_one(selector="#name")  # using id selectors
# print(name)
#
# # using class selectors
# heading_elements = soup.select(".heading")
# print(heading_elements)

""" The selectors can be passed directly as arguments without using selector= """

# Live site WebScraping on ycombinator.com

response = requests.get("https://news.ycombinator.com/news")

yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")
# print(soup.title)

articles = soup.find_all(name="span", class_="titleline")  # ignore the typo in the class name
article_texts = []
article_links = []

# ## !!! original method from the course does not work due to changes to website !!! ###

for article_tag in articles:
    # find the "a" tag inside the "span" name declared above
    a_tag = article_tag.find('a')
    # if "a" tag is found => extract "text" and "href" attributes
    if a_tag:
        text = a_tag.getText()
        link = a_tag.get('href')
        # append to list
        article_texts.append(text)
        article_links.append(link)


# this will result in a list of elements
# ResultSet object has no attribute 'getText'. used list comprehension to get the text
score_source = soup.find_all(name="span", class_="score")
article_votes = [int(element.getText().split()[0]) for element in score_source]

# apply the split to above list comprehension
# print(int(article_votes[0].split()[0]))  # splitting the score to get the number

print(article_texts)
print(article_links)
print(article_votes)

# extract the article with the most votes.
largest_number = max(article_votes)
print(largest_number)
largest_index = article_votes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(article_votes[largest_index])

# ## !!! in the navbar after the site url add /robots.txt !!! ##
# ## !!! this will allow to see what is allowed and disallowed to webscrape !!! ##
# ## !!! account for scraping loops and constant calls -> make it, so it has a delay of 1 min at least !! ##

