from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import random

SIMILAR_ACCOUNT = "molalign.5"
USERNAME = os.environ.get("IG_USERNAME")
PASSWORD = os.environ.get("IG_PASSWORD")


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 15)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        try:
            decline_cookies_xpath = "//button[text()='Decline optional cookies']"
            cookie_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, decline_cookies_xpath)))
            cookie_btn.click()
        except TimeoutException:
            pass
        username = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        try:
            save_login_prompt = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now')]"))
            )
            save_login_prompt.click()
        except TimeoutException:
            pass

        try:
            notifications_prompt = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            notifications_prompt.click()
        except TimeoutException:
            pass

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        modal = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog'] ul")))

        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(random.uniform(1.5, 3.0))  

    def follow(self):
        all_buttons = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='dialog'] ul button"))
        )

        for button in all_buttons:
            try:
                button.click()
                time.sleep(random.uniform(2, 5))  
            except ElementClickInterceptedException:
                try:
                    cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
                except:
                    pass

    def quit(self):
        self.driver.quit()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
bot.quit()
