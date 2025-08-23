from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com")

wait = WebDriverWait(driver, 20)

sleep(8)

for _ in range(70):  
    try:
        buttons = driver.find_elements(By.CLASS_NAME, "gamepad-icon-wrapper")

        like_btn = buttons[2]

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "gamepad-icon-wrapper")))
        like_btn.click()
        print("Liked a profile")
    except Exception as e:
        print("Error clicking like:", e)

    sleep(2)
