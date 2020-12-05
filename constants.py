PATH = '/usr/bin/chromedriver'
with open('env.txt', 'r') as secrets:
    data = secrets.readline()
    name = data.split(':')[0]
    password = data.split(':')[1]

TWITTER_NUMBER = name
TWITTER_PASSWORD = password
URL = "https://twitter.com"
PROMISE_UP = 10
PROMISE_DOWN = 150
