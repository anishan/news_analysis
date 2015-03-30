""" Article Class used in News Bias Program """

class Article(object):
    """ Stores the information for each article to be analyzed """
    def __init__(self, url, tags):
        """ url: the url of the website
            tags: the relevant html tags to strip
            contents: the text of the article
        """
        self.url = url
        self.tags = tags
        #self.contents

    def __repr__(self):
        """ Returns article text """
        return self.url
