from twython import TwythonStreamer

APP_KEY="Vp0UrPOKfUDonEn4B5RCpg"
APP_SECRET="3wdvhsj1ph2PiNi1E47XullWsaEEZpepMPh4bgOCMY"
OAUTH_TOKEN="634391884-qFKI6JYrZV6JFQYHIFhConcn7S1Se86SP0YHHWDt"
OAUTH_TOKEN_SECRET="zcUKICiN4GWYrS7cyOBHyiJCHqeyjMGn3J7GfwVWrZ8"


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
        # Want to disconnect after the first result?
        # self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data

# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(track='twitter')
#stream.statuses.filter(follow='16414559')
#stream.user()  # Read the authenticated users home timeline (what they see on Twitter) in real-time
#stream.site(follow='luzm')
