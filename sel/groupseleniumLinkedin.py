from selenium import webdriver
from random import *
from .utils import wait_rand, wait_to_load, press_rand, login, driver

# options = webdriver.ChromeOptions()
# options.add_argument('headless')

# # set the window size
# options.add_argument('window-size=1200x600')

# # initialize the driver
# driver = webdriver.Chrome(chrome_options=options)

def post_to_group():
	
	groups = input('Insert group name: ')
	# title = input('Insert title: ')
	# comment = input('Insert text: ')
    
	button = driver.find_element_by_css_selector('button[data-control-name="nav.launcher"]')
	button.click()

	wait_rand()	

	button = driver.find_element_by_css_selector("a[data-control-name='nav.launcher_groups']")
	button.click()
	
	driver.switch_to_window(driver.window_handles[1])

	wait_rand()

	button = driver.find_element_by_css_selector('a[href="/groups/my-groups"]')
	button.click()

	wait_to_load()
	driver.get_screenshot_as_file('img/2-my-groups.png')

	button = driver.find_element_by_xpath('//*[contains(text(), "Hard Workers from MD")]')
	button.click()

	wait_rand()	
	
	input = driver.find_element_by_css_selector('input[name="title"]')
	input.send_keys("new title")
	
	wait_rand()

	input = driver.find_element_by_css_selector('textarea[name="body"]')
	input.send_keys("new body here @sergh")

	driver.get_screenshot_as_file('img/3-in-group.png')


def post_to_page():
	default_button = driver.find_element_by_css_selector('a[href="/feed/"]')
	default_button.click()

	button = driver.find_element_by_css_selector('button[data-control-name="share.post"]')
	button.click()

	input = driver.find_element_by_xpath("//div[@role='textbox']")
	input.send_keys(" @Deeplace")

	select = driver.find_element_by_css_selector('ul.mentions-search-results li.mentions-search-item')
	select.click()

	driver.get_screenshot_as_file('img/1-on-page.png')
