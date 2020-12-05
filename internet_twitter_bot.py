from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from constants import PATH, URL, TWITTER_PASSWORD, PROMISE_UP, TWITTER_NUMBER, PROMISE_DOWN


class InternetTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=PATH)
        self.driver.get(URL)
        # print(TWITTER_PASSWORD)

        self.up_speed = 0
        self.down_speed = 0

    def get_internet_speed(self):
        sleep(3)
        self.driver.get('https://www.speedtest.net/')
        start_test = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_test.click()
        sleep(60)
        down_speed = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        down_speed = down_speed.text
        self.down_speed = float(down_speed)

        up_speed = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        up_speed = up_speed.text
        self.up_speed = float(up_speed)
        print('up speed :' + up_speed, '\ndown speed :' + down_speed)

    def tweet_at_provider(self):
        x_path = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[' \
                 '2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/span/span '
        if self.up_speed < PROMISE_UP and self.down_speed < PROMISE_DOWN:
            self.driver.get(URL)
            click_button = self.driver.find_element_by_link_text('Log in')
            click_button.click()

            username = self.driver.find_element_by_name('session[username_or_email]')
            username.send_keys(TWITTER_NUMBER)
            password = self.driver.find_element_by_name('session[password]')
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            write_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div['
                                                            '2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div['
                                                            '1]/div/div/div/div[2]/div['
                                                            '1]/div/div/div/div/div/div/div/div/div/div['
                                                            '1]/div/div/div/div/div/div/div/div/span/span')
            write_tweet.send_keys(f"My internet upload speed  is {self.up_speed}, and Download Speed is {self.down_speed}. "
                                  f"I am using Zong. By the way I am PY-BOT. Contact Him for Automation with Python")
            submit = self.driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                        '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                        '4]/div/div/div[2]/div')
            submit.click()


