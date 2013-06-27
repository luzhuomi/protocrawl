from twython import Twython, TwythonError

APP_KEY="MqmC445PgdRcL3kGOV1jlA"
APP_SECRET="uVoRVMRAb4i3rJzISTiksikC6fD48xavIIXDuSpDU"
OAUTH_TOKEN="1544677256-8miH8PS8ScFweMCNAONDSqzzkxYRGx0KrnJ2BSZ"
OAUTH_TOKEN_SECRET="IZLkA9uivhHWdXmz4IRXHCVo2JWq6Ic6e5eTrhVpcg"



# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
    user_timeline = twitter.get_user_timeline(screen_name='royalplazatweet')
except TwythonError as e:
    print e

print user_timeline
print len(user_timeline)
