from XUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class X:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs", {"intl.accept_languages": ["en-US", "en"]})
        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://x.com/i/flow/login")
        time.sleep(5)

        # Kullanıcı adı alanı
        input_username = self.browser.find_element(By.NAME, "text")
        input_username.send_keys(self.username)
        input_username.send_keys(Keys.ENTER)
        time.sleep(5)

        # Şifre alanı
        input_password = self.browser.find_element(By.NAME, "password")
        input_password.send_keys(self.password)
        input_password.send_keys(Keys.ENTER)
        time.sleep(5)

    def search(self, hashtag):
        searchInput = self.browser.find_element(By.XPATH,
                                                "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input")
        searchInput.send_keys(hashtag)
        time.sleep(5)

        searchInput.send_keys(Keys.ENTER)
        time.sleep(5)

        loop_counter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loop_counter > 4:
                break
            self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(3)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loop_counter += 1

        tweets = self.browser.find_elements(By.XPATH, "//div[@data-testid='cellInnerDiv']")
        print(f"{len(tweets)} adet tweet bulundu.\n")

        with open("tweetler.txt", "w", encoding="utf-8") as dosya:
            for tweet in tweets:
                try:
                    text_element = tweet.find_element(By.XPATH, ".//div[@data-testid='tweetText']")
                    text = text_element.text.strip()
                    if text:
                        print("Tweet:", text)
                        print("----------------------------")
                        dosya.write(text + "\n")
                        dosya.write("----------------------------\n")
                except:
                    pass


X = X(username, password)
X.signIn()
X.search("Python")
