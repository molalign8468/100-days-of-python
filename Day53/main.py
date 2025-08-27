import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class ZillowFormBot:
    def __init__(self, form_url, listings_url):
        self.form_url = form_url
        self.listings_url = listings_url
        self.driver = self._setup_driver()
        self.address_inp = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.price_inp = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.link_inp = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.submit_btn = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
        self.after_submission = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'

    def _setup_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.form_url)
        return driver

    def scrape_listings(self):
        response = requests.get(self.listings_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find_all(name="article", class_="StyledPropertyCard-c11n-8-84")

    def add_form(self, address, price, link):
        property_address = self.driver.find_element(By.XPATH, self.address_inp)
        property_address.send_keys(address)

        property_price = self.driver.find_element(By.XPATH, self.price_inp)
        property_price.send_keys(price)

        property_link = self.driver.find_element(By.XPATH, self.link_inp)
        property_link.send_keys(link)

        submit = self.driver.find_element(By.XPATH, self.submit_btn)
        submit.click()
        sleep(2)

        new_form = self.driver.find_element(By.XPATH, self.after_submission)
        new_form.click()

    def run(self):
        articles = self.scrape_listings()
        for card in articles:
            link = card.find(name="a", class_="StyledPropertyCardDataArea-anchor").get("href")
            address = card.find(name="address").get_text().strip()
            price = card.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").get_text()
            sleep(1)
            self.add_form(address, price, link)


if __name__ == "__main__":
    google_form_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdmRC1yAcoXKH4pCCE4Ar7SMQgp3pmOzTDi0m-1_t8nNABTIw/viewform?usp=dialog"
    zillow_URL = "https://appbrewery.github.io/Zillow-Clone/"

    bot = ZillowFormBot(google_form_URL, zillow_URL)
    bot.run()
