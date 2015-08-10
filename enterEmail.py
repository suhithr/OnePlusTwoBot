from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

kolid = "OPFH0P0"

driver = webdriver.Firefox()
driver.get("https://oneplus.net/invites?kolid=" + kolid)
assert "OnePlus Invites - OnePlus.net" in driver.title
emailInput = driver.find_element_by_id("email")

mail = "se.ve.nthdreamofte.en.ag.eh.eaven"
emailInput.send_keys(mail + "@gmail.com")
time.sleep(8)
submitButton = driver.find_element_by_id("submit_email")
submitButton.click()
time.sleep(10)
driver.close()
