from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

print("Looking for language selection...")
try:
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3) 
except NoSuchElementException:
    print("Language selection not found")

sleep(2)

cookie = driver.find_element(by=By.ID, value="bigCookie")

item_ids = [f"product{i}" for i in range(18)]

wait_time = 5
timeout = time() + wait_time  
five_min = time() + 60 * 5  

while True:
    cookie.click()

    if time() > timeout:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text

            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):  
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break