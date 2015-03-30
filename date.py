""" Date Class used in News Bias Program """

# Import
from jdcal import gcal2jd


class Date(object):
    """ Represents a particular day on the calendar """
    def __init__(self, month, day, year):
        """ month: the month (represented as an integer in [1,12])
            day: the day of the month (represented as an integer)
            year: the year (represented as an integer)
            This method will not validate whether a given date is invalid
            (e.g. April 31, 2000) """
        self.month = month
        self.day = day
        self.year = year
        self.jdate = self.convert_jd()

    def __str__(self):
        """ Converts the date to a string in the following format:
            Month, Day Year (where Month is the name of the month, e.g. January)
        """
        months = ['January', 'Febraury', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November',
                  'December']
        month = months[self.month - 1]
        string = "%s %s, %s" % (month, self.day, self.year)
        return string                  

    def convert_jd(self):
        """ Returns the date stored in the object in the julian date format
        """
        a, b = gcal2jd(self.year, self.month, self.day)
        jdate = a + b
        return int(jdate)

