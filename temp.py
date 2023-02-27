from selenium import webdriver
import time
from selenium.webdriver.common.by import By

in_stoc = "https://myebox.ro/produs/elastice-din-cauciuc-set-90g/"
stoc_limitat = "https://myebox.ro/produs/set-capse-metalice-banda-pp-16-mm-2000-buc-cutie/"
lipsa_stoc = "https://myebox.ro/produs/rigla-aluminiu-30-cm/"
selectii_multiple = "https://myebox.ro/produs/tus-pentru-stampila-pe-baza-de-apa/"

browser = webdriver.Chrome()
browser.get(lipsa_stoc)

time.sleep(2)

# # pentru paginile cu produse in stoc
# stoc = browser.find_element(By.XPATH, "//input[@title='Cantitate']").get_attribute("max")
# print(stoc)

# # pentru paginile cu stoc limitat
# stoc = browser.find_element(By.XPATH, "(//p[@class='stock in-stock'])[1]").get_attribute("innerHTML").split("Doar ")[1].split(" ")[0]
# print(stoc)

# pentru paginile cu produse out of stock
stoc = browser.find_element(By.XPATH, "//p[@class='stock out-of-stock']").get_attribute("class").lstrip("stock").strip()
print(stoc)

# # pentru paginile cu selectii multiple
# stoc = browser.find_element(By.XPATH, "(//table[@class='variations'])[1]").get_attribute("outerHTML")
# # print(x.get_attribute("outerHTML"))
# if "Alege o opțiune" in stoc:
#     print("Selectii multiple")