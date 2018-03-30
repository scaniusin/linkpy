from selenium import webdriver
from random import *
from openpyxl import load_workbook
import time
import json

options = webdriver.ChromeOptions()
# options.add_argument('headless')

# set the window size
options.add_argument('window-size=1600x1200')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

driver.set_page_load_timeout(20)
driver.implicitly_wait(10)
driver.set_script_timeout(10)

def wait_rand():
	time.sleep(uniform(2, 6))
def wait_to_load():
	time.sleep(5)

# try:
#    element_present = EC.presence_of_element_located((By.ID, 'whatever'))
#    WebDriverWait(driver, timeout).until(element_present)
# except TimeoutException:
#     print "Timed out waiting for page to load"

def press_rand():
	driver.refresh() #to change

	home = driver.find_element_by_css_selector('a[href="/feed/"]')
	myNetwork = driver.find_element_by_css_selector('a[href="/mynetwork/"]')
	jobs = driver.find_element_by_css_selector('a[href="/jobs/"]')
	messaging = driver.find_element_by_css_selector('a[href="/messaging/"]')
	notifications = driver.find_element_by_css_selector('a[href="/notifications/"]')

	wait_rand()

	buttons = [home, myNetwork, jobs, messaging, notifications]
	buttons[randrange(1, 5)].click()
	
	wait_rand()

	driver.get_screenshot_as_file('img/3-rand-press.png')


def login(email_input, password_input):
	# email_input = input('Insert account email: ')
	# password_input = input('Insert account password: ')
	
	driver.get("https://www.linkedin.com/")
	
	wait_to_load()

	email = driver.find_element_by_css_selector('#login-email')
	password = driver.find_element_by_css_selector('#login-password')
	login = driver.find_element_by_css_selector('#login-submit')

	email.send_keys(email_input)
	password.send_keys(password_input)
	
	login.click()

	wait_to_load()

	driver.get_screenshot_as_file('img/0-login-success.png')


def load_linkedIn_links_from_file():
	wb = load_workbook(filename = 'links.xlsx')
	ws = wb['Sheet 1']
	accounts = []
	for row in ws.rows:
		# list_links.append(row[0].value)
		account = {}
		account['id'] = row[0].value
		account['link'] = row[1].value
		accounts.append(account)
	
	return accounts
