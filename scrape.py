# webscraping library
import lxml.html
import requests

import urllib2
# another option for webscraping library
from bs4 import BeautifulSoup, SoupStrainer
import itertools


# this is just copied from an old repo, i don't think its exactly what we want. but just a template
# response = urllib2.urlopen("http://unicode.org/emoji/charts/full-emoji-list.html")
# emoji_html = response.read()
# only_names = SoupStrainer(attrs={"class": "name"})
# only_codes = SoupStrainer(attrs={"class": "code"})


# soup_names = BeautifulSoup(emoji_html,"html.parser",parse_only=only_names)
# soup_codes = BeautifulSoup(emoji_html,"html.parser",parse_only=only_codes)

# emoji_d_name = {}
# emoji_d_code = {}

# for name,code in itertools.izip(soup_names.strings,soup_codes.strings):
# 	emoji_d_name[name] = code
# 	emoji_d_code[code] = name
