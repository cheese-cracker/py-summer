"""
Originally, Used to scrape contents of <div> tags of a specific class
Now, it scrape contents of other tags (without class)
"""
import requests
import re
from bs4 import BeautifulSoup
from sys import stdout

"""Remove whitespaces from Text"""
def whiteWash(text):
    whitespacer = re.compile('\S+')
    plain_text = list(filter(whitespacer.search, text))
    return ''.join(plain_text)


"""Scrape and print <_> tag of attribute class = _"""
def div_scrape(Soup, scrape_type):
    tag_class = input("class to scrape: ")
    val = [item.text for item in Soup.find_all(scrape_type, {'class': tag_class})]
    return ''.join(val)


"""Scape and print <_> tag contents"""
def tag_scrape(Soup, scrape_type):
    val = [item.text for item in Soup.find_all(scrape_type)]
    return ''.join(val)



# url with http:// and / ending!
url = input("Extract Url: ")
scrape_type = input("Tag to scrape (div/p): ")

# url = "www.pythonforbeginners.com/"
# div_class = "post-bodycopy cf"

req = requests.get(url)
Soup = BeautifulSoup(req.text, "html.parser")

if scrape_type == 'div':
    content = div_scrape(Soup, scrape_type)
else:
    content = tag_scrape(Soup, scrape_type)


# content = Soup.get_text()

stdout.write((whiteWash(content)))
print('\n')
