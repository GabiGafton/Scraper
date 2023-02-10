from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://myebox.ro/categorii/accesorii-de-impachetat/")

time.sleep(5)
height = browser.execute_script("return document.body.scrollHeight;")
print(height)

links = set()
for x in range(10):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    new_height = browser.execute_script("return document.body.scrollHeight;")
    print(new_height)
    if new_height == height:
        break
    height = new_height
    products = browser.find_elements(By.CSS_SELECTOR, "div > div > h3 > a")
    for i in products:
        links.add(i.get_attribute("href"))

print(len(links))
browser.refresh()
time.sleep(3)

for x in links:
    time.sleep(3)
    try:
        browser.get(x)
        product_title = browser.find_element(By.CSS_SELECTOR, "head > title")
        print(product_title.get_attribute("innerHTML"))
        product_stoc = browser.find_element(By.CLASS_NAME, "quantity")
        stoc = (product_stoc.get_attribute("innerHTML")).split('max="')[1].split('"')[0]
        print(stoc)
    except:
        stoc = 1
        print(stoc)

# browser.close()