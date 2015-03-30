# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25

@author: Anisha Nakagawa

Search for news articles for a given event through a set of pre-defined websites

"""

# Import Packages
# To get html from websites:
from pattern.web import URL, plaintext, strip_between, Google

g = Google()
for result in g.search("People's Climate March"):
    print result.url
    print plaintext(result.text)
    print result.date


#people's climate march site:usatoday.com daterange:2456921-2456923
