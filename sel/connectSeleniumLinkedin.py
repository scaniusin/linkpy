from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from .utils import *
import json
from random import *

LIMIT = randrange(30, 50) #to change


def send_connect(lead, account_email):	
	if lead['link']:
		driver.get(lead['link'])
		log_file("load link", lead['link'])
		wait_to_load()	
	else:
		return
		
	try:
		available = driver.find_element_by_css_selector('div.profile-unavailable')	
		log(lead, 'account deleted', account_email)
		driver.get_screenshot_as_file('img/profile-unavailable-' + lead['link'] + '.png')
		log_file("profile is unavailable", available)
		return
	except NoSuchElementException:
		log_file("profile is available", NoSuchElementException)
		pass
	
	try:
		status = driver.find_element_by_css_selector('span.pv-s-profile-actions__label').text
		log_file("check status", status)
		driver.get_screenshot_as_file('img/1_add-new-connect.png')
	except NoSuchElementException:
		log_file("no status element", NoSuchElementException)
		log(lead,'account not found', account_email)
		driver.get_screenshot_as_file('img/profile-unavailable-' + lead['link'] + '.png')
		return

	if status == "Connect":
		button = driver.find_element_by_css_selector('button.pv-s-profile-actions--connect')
		button.click()
		log(lead, 'Sent', account_email)
	elif status == "Message":
		log(lead, 'Connected', account_email)
		return
	elif status == "InMail":
		log(lead, status, account_email)
		return
	elif status == "Pending":		
		log(lead, status, account_email)
		return
	else:
		driver.get_screenshot_as_file('img/ERROR-' + lead['link'] + '.png')
		return

	name = driver.find_element_by_css_selector('h1.pv-top-card-section__name').text
	text = "Hello " + name + ", can we connect on Linkedin?"

	log_file("get profile name", name)

	button = driver.find_element_by_css_selector('button.mr1')
	button.click()

	log_file("click button connect", button)

	wait_rand()

	textarea = driver.find_element_by_css_selector('textarea.send-invite__custom-message')
	textarea.send_keys(text)

	log_file("fill textarea", textarea)

	wait_to_load()

	button = driver.find_element_by_css_selector('button.ml1')
	button.click()

	log_file("click button send", button)

	wait_to_load()

	driver.get_screenshot_as_file('img/2_' + name + '_sent.png')

	press_rand()


def connect():
	log_file("\n\n START of Script Connection \n", None)
	accounts = json.load(open('accounts.json'))
	portion = 0
	
	while(True):
		for account in accounts:
			log_file("random profiles to import", LIMIT)
			log_file("number of portion to import", portion)
			leads = load_linkedIn_links_from_file(account['file'], LIMIT, portion)
			log_file("load leads", leads)
			if leads:
				log_file("login as", account['email'])
				login(account['email'], account['password'])
				for lead in leads:
					try:
						send_connect(lead, account['email'])
					except ValueError:
						log_file("Handled ERROR", ValueError)
						driver.get_screenshot_as_file('img/error-' + lead['link'] + '.png')
						continue
				logout()
			elif accounts.index(account) == len(accounts)-1:
				log_file("SUCCESS", None)
				return
		portion+=1
		log_file("waiting 5 min", None)
		wait_in_min(5) #change
	
