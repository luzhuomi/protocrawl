
from string import replace
import datetime


def normalizeFriendlyDate(s):
    todaystr = str(datetime.date.today())
    yesterdaystr = str(datetime.date.today()-datetime.timedelta(days=1))
    return replace(replace(s.upper(), 'TODAY', todaystr), 'YESTERDAY', yesterdaystr)
