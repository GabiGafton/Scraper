from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.by import By
import openpyxl

in_stoc = "https://myebox.ro/produs/elastice-din-cauciuc-set-90g/"
stoc_limitat = "https://myebox.ro/produs/dispozitiv-manual-milano-de-legat-banda-pp-16-mm/"
lipsa_stoc = "https://myebox.ro/produs/rigla-aluminiu-30-cm/"

browser = webdriver.Chrome()
browser.get(stoc_limitat)

time.sleep(2)

# # pentru paginile cu produse in stoc
# x = browser.find_element(By.XPATH, "(//p[@class='stock in-stock'])[1]")
# print(x.get_attribute("class"))
#
# x = browser.find_element(By.XPATH, "//input[@title='Cantitate']")
# print(x.get_attribute("max"))

# pentru paginile cu stoc limitat
x = browser.find_element(By.XPATH, "(//p[@class='stock in-stock'])[1]")
print(x.get_attribute("class"))

x = browser.find_element(By.XPATH, "//p[@class='stock in-stock']")
print(x.get_attribute("innerHTML"))
stoc = x.get_attribute("innerHTML").split("Doar ")[1].split(" ")[0]
print(stoc)

# # pentru paginile cu produse out of stock
# x = browser.find_element(By.XPATH, "//p[@class='stock out-of-stock']")
# stoc = x.get_attribute("class").lstrip("stock").strip()
# print(stoc)

