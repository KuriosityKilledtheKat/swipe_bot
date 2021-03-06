from selenium import webdriver
import sys
sys.path.append('/Users/AaronLee/Documents/GitHub/creds')
from login_info import username, password
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/AaronLee/Documents/GitHub/chromedriver')

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()                              

        # switch to login popup
        base_window = self.driver.window_handles[0]
        popup = self.driver.window_handles[1]
        self.driver.switch_to.window(popup)

        sleep(0.5)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)


        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(3)
        # switch to original window

        self.driver.switch_to.window(base_window)

        loc_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        loc_popup.click()

        notif_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notif_popup.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def match_popup(self):
        m_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span')
        m_btn.click()

    def homescreen_popup(self):
        hs_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span')
        hs_btn.click()

    def plus_popup(self):
        plus_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        plus_popup.click()

    def auto_swipe(self):
        count = 0
        matches = 0
        while True:
            sleep(1)
            try:
                self.like()
                count += 1
                print ('Like Counter: {} |  Match Counter: {}'.format(count, matches))
            except Exception:
                sleep (0.5)
                try:
                    self.homescreen_popup()

                except Exception:
                    try:
                        self.homescreen_popup()
                        matches += 1
                        print ('---> Match Counter: {} <---'.format(matches))
                    except Exception:
                        self.plus_popup()
                        count -= 1

    

    def send_messages(self):
        match_btn = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[2]/a/div[1]')
        match_btn.click()

        # You can change the message to say whatever you want
        message_in = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        message_in.send_keys('I was told to expand my job search, so I did. Hi Im Aaron!')

        send_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button/span')
        send_btn.click()

    def match_tab(self):
        mt_btn = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
        mt_btn.click()


    # automatically messages people
    def auto_message(self):
        sent = 0
        while True:
            sleep(0.5)
            try:
                self.match_tab()
                self.send_messages()
                sent += 1
                print ('Messages sent: {}'.format(sent))
            except Exception:
                pass


bot = TinderBot()
bot.login()
sleep(7)
bot.auto_swipe()
bot.auto_message()