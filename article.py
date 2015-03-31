""" Article Class used in News Bias Program """

# Import stuff
from pattern.web import URL, plaintext, strip_between

class Article(object):
    """ Stores the information for each article to be analyzed """
    def __init__(self, url, tags):
        """ url: the url of the website
            tags: the relevant html tags to strip
            contents: the text of the article
        """
        self.url = url
        self.tags = tags
        self.contents = self.get_contents()

    def __repr__(self):
        """ Returns article text """
        return self.contents

    def get_contents(self):
        """ Returns the article contents by reading in the html from the
            url, stripping away the tags, and returning a string of text
        """
        text = URL(self.url).download()

        # Strip out text between the specific tags
        for t in self.tags:
            text = strip_between(t[0], t[1], text)

        # Strip out general html formatting and convert to proper text form
        text = plaintext(text)
        text = text.encode('utf8')
        return text
