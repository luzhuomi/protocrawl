from twython import Twython, TwythonError

# Requires Authentication as of Twitter API v1.1
APP_KEY="Vp0UrPOKfUDonEn4B5RCpg"
APP_SECRET="3wdvhsj1ph2PiNi1E47XullWsaEEZpepMPh4bgOCMY"
OAUTH_TOKEN="634391884-qFKI6JYrZV6JFQYHIFhConcn7S1Se86SP0YHHWDt"
OAUTH_TOKEN_SECRET="zcUKICiN4GWYrS7cyOBHyiJCHqeyjMGn3J7GfwVWrZ8"

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
    user = twitter.lookup_user(screen_name='ryanmcgrath,luzm')
except TwythonError as e:
    print e

print user
