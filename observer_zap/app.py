from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
url_whats = ""
driver.get("https://web.whatsapp.com")
sleep(100)

driver.close()