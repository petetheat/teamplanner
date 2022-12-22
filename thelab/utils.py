from calendar import HTMLCalendar
import calendar


WEEK_DAY_DICT = dict(zip(range(7), calendar.day_abbr))


class Calendar(HTMLCalendar):
    def __init__(self):
        super(Calendar, self).__init__()

