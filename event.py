""" Event Class used in News Bias Program """

from date import *
from pickle import dump, load
from pattern.web import Google
from os.path import exists
from article import *

class Event(object):
    """ Stores data about an event that will be analyzed """
    def __init__(self, name, date):
        """ name: name of the event as it would be searched
            date: date object for the date the event occured
            articles: dictionary with news sources as the key,
            and Article objects as the values
        """
        self.name = name
        self.date = date
        self.articles = self.get_articles()

    def __str__(self):
        """ Returns the event and date """
        return self.name + ": " + str(self.date)

    def get_articles(self):
        """ Gets the articles for the particular event for each news source
            contained in the file news_sources.txt, read in by pickle.
            returns a dictionary with the news source as the key and article
            object as the value
        """
        # Article list will be stored in txt file named by the event
        filename = self.name + ".txt"

        # If the event has already been searched, return the saved articles
        if exists(filename):
            return load(open(filename, "r+"))

        # Otherwise, search for the correct urls and parse text,
        # then create Article objects and save to list
        articles = []
        # Dictionary of news sources and tags to search
        news_sources = load(open('news_sources.txt', "r+")) 
        for s in news_sources:
            try:
                url = self.get_url(s)
                tags = news_sources[s]
                articles.append(Article(url, tags))
            except:
                print "No valid article for ", s

        # Write the list of articles to a text file
        dump(articles, open(filename, 'w'))

        return articles
    
    def get_url(self, s):
        """ Returns the best url for the news source about the event """
        g = Google()
        # Format information into google search format
        search_term = self.get_search_term(s)
        # Get the url by going through google search results
        for result in g.search(search_term):
            url = result.url
            # Check if valid url
            if self.is_valid_url(url):
                return url
        # If there is nothing valid throw an error
        raise ValueError('No articles fit criteria')
        
    def get_search_term(self, s):
        """ Format information into google search format """
        site = " site:" + s + " "
        
        start_date = self.date.convert_jd()
        end_date = start_date + 2
        date_range = 'daterange:' + str(start_date) + '-' + str(end_date)
        
        search_term = self.name + site + date_range
        return search_term

    def is_valid_url(self, url):
        """ Checks to see if a url is valid """
        # Valid urls should not contain the terms in this list
        invalid_terms = ['blogs', 'opinion', 'gallery', 'photos']
        for t in invalid_terms:
            if t in url:
                return False
        return True


        
