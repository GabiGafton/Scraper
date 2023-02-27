from selenium import webdriver
import time
from selenium.webdriver.common.by import By

in_stoc = "https://myebox.ro/produs/elastice-din-cauciuc-set-90g/"
stoc_limitat = "https://myebox.ro/produs/set-capse-metalice-banda-pp-16-mm-2000-buc-cutie/"
lipsa_stoc = "https://myebox.ro/produs/rigla-aluminiu-30-cm/"
selectii_multiple = "https://myebox.ro/produs/tus-pentru-stampila-pe-baza-de-apa/"
atipic_00 = "https://myebox.ro/produs/cutie-transport-1-sticla-de-vin-cu-separator-inclus/"
atipic_01 = "https://myebox.ro/produs/banda-adeziva-umectibila-din-hartie-kraft-ecologica-50mm-x-55-yds/"
atipic_02 = "https://myebox.ro/produs/banda-adeziva-fragil-red-silentioasa-48-mm-x-66-m/"
atipic_03 = "https://myebox.ro/produs/banda-de-legat-pp-12-mm-2500-m-10-kg/"
atipic_04 = "https://myebox.ro/produs/hartie-fagure-kraft-0-20mx250m/"

browser = webdriver.Chrome()
browser.get(atipic_04)

time.sleep(2)

try:
    # pentru paginile cu produse in stoc
    stoc = browser.find_element(By.XPATH, "//input[@title='Cantitate']").get_attribute("max")
    if stoc.isdigit():
        print("produs in stoc: ", stoc)
    else:
        print("N\\A")
except:
    pass

try:
    # pentru paginile cu stoc limitat
    stoc = browser.find_element(By.XPATH, "(//p[@class='stock in-stock'])[1]").get_attribute("innerHTML").split("Doar ")[1].split(" ")[0]
    print("produs cu stock limitat: ", stoc)
except:
    pass

try:
    # pentru paginile cu produse out of stock
    stoc = browser.find_element(By.XPATH, "//p[@class='stock out-of-stock']").get_attribute("class").lstrip("stock").strip()
    print(stoc)
except:
    pass

try:
    # pentru paginile cu selectii multiple
    stoc = browser.find_element(By.XPATH, "(//table[@class='variations'])[1]").get_attribute("outerHTML")
    # print(x.get_attribute("outerHTML"))
    if "Alege o opțiune" in stoc:
        print("Selectii multiple")
except:
    pass

try:
    # pentru paginile cu produse promo
    stoc = browser.find_element(By.XPATH, "//strong[normalize-space()='Disponibil începand cu 1 Martie pe MyEbox.ro']").get_attribute("outerHTML").split("<strong>")[1].rstrip("</strong>")
    # print(x.get_attribute("outerHTML"))
    print(stoc)
except:
    pass