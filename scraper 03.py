from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://myebox.ro/produs/plic-curierat-awb-autoadeziv-c6-114-x-162-mm/")

product_title = browser.find_element(By.CSS_SELECTOR, "head > title")
print(product_title.get_attribute("innerHTML"))

product_stoc = browser.find_element(By.CLASS_NAME, "quantity")
stoc = (product_stoc.get_attribute("innerHTML")).split('max="')[1].split('"')[0]
print(stoc)
