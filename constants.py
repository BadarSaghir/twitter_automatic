import os
PATH = '/usr/bin/chromedriver'


TWITTER_NUMBER = os.environ.get('USER_NUMBER')
TWITTER_PASSWORD = os.environ.get('PASSWORD')
URL = "https://twitter.com"
PROMISE_UP = 10
PROMISE_DOWN = 150
print(TWITTER_NUMBER, TWITTER_PASSWORD)