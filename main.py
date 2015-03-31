""" Main File for News Bias Program """

from pickle import dump, load

def write_news_sources():
    """ Writes a file with a dictionary of the news sources and a list of
        the corresponding tags using pickle.
        returns the dictionary
    """
    news_sources = {'BBC.com': [('<footer', '</footer>'), ('<nav', '</nav>'), ('<header', '</header>'), ('<a', '</a>'), ('<span', '</span>'), ('<meta', '/>'), ('<div id="most-popular"', '</div>'), ('<li', '</li>'), ('<span', '</span>'), ('<button', '</button>')],
                    'NPR.org': [('<footer', '</footer>'), ('<nav', '</nav>'), ('<header', '</header>'), ('<a', '</a>'), ('<span', '</span>'), ('<div id="commentBlock">', '</div>'), ('<div class="adwrap">', '</div>')],
                    'FoxNews.com': [('<footer', '</footer>'), ('<nav', '</nav>'), ('<header', '</header>'), ('<span', '</span>'), ('<div id="user-options"', '</span'), ('<div id="subscribe', '</div>'), ('<div class="subscribe', '</div>'), ('<p class="advert-txt">', '</p>')],
                    'CNN.com': [('<footer', '</footer>'), ('<nav', '</nav>'), ('<header', '</header>'), ('<a', '</a>'), ('<span', '</span>'), ('<div class="cd__description"', '</div>'), ('<div class="js-el__gallery', '</div>'), ('<div class="el__gallery','</div>')],
                    'Economist.com': [('<footer', '</footer>'), ('<nav', '</nav>'), ('<header', '</header>'), ('<a', '</a>'), ('<span', '</span>'), ('<strong','/strong>'), ('<li', '</li>'), ('<div class="title">', '</div>'), ('<div class="about">', '</div>'), ('<div class="product', '</div>')],
                    'BostonGlobe.com': [('<footer', '</footer>'), ('<nav', '</nav>'), ('<header', '</header>'), ('<a', '</a>'), ('<span', '</span>'), ('<li', '</li>'), ('<span', '</span>'), ('class="bg', '</'), ('<button', '</button>'), ('<div class="fineprint', '</'), ('="email', '</'), ('<div class="tease-text">', '</div>'), ('<div class="paywall', '</div>')],
                    'Yahoo.com': [('<footer', '</footer>'), ('<nav', '</nav>'), ('<header', '</header>'), ('<a', '</a>'), ('<span', '</span>'), ('<li', '</li>'), ('<span', '</span>')],
                    'USAToday.com': [('<footer', '</footer>'), ('<nav', '</nav>'), ('<header', '</header>'), ('<a', '</a>'), ('<span', '</span>'), ('<li', '</li>'), ('<span', '</span>'), ('class="share','</'), ('class="util','</')],
                    }
    dump(news_sources, open('news_sources.txt', 'w'))
    return news_sources

#counter = load(open('news_sources.txt', "r+"))
#print counter

#write_news_sources()
