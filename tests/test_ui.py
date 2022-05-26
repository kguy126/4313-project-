from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time 

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://dev.yuride.network")

try:

	l= driver.find_element_by_tag_name("title")
	s= driver.title
	print("Title is" + s)
	
except NoSuchElementException:
	print("Element does not exist")

	driver.close()

link = driver.find_element_by_link_text("Sign In")
link.click()

element = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID, "mli"))
)
username = driver.find_element_by_id("mli")

password = driver.find_element_by_id("password")

username.send_keys("")

password.send_keys("")

linkk = driver.find_element_by_name("dologin")
linkk.click()


element = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.row.p-4.m-4"))
)
try:

	l= driver.find_element_by_css_selector("h1")
	s= l.text
	print("Element exist -" + s)
	
except NoSuchElementException:
	print("Element does not exist")

	driver.close()
	


