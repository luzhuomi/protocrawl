from weibo import APIClient

APP_KEY = '475274177' # app key
APP_SECRET = '71e3a5218f1dd10a4e7833415ac87509' # app secret
CALLBACK_URL = 'http://sites.google.com/site/luzhuomi/'


client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
