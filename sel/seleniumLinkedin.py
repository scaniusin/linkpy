from selenium import webdriver
from .utils import wait_rand, wait_to_load, press_rand, login, load_linkedIn_links_from_file, driver

# options = webdriver.ChromeOptions()
# options.add_argument('headless')

# # set the window size
# options.add_argument('window-size=1200x600')

# # initialize the driver
# driver = webdriver.Chrome(chrome_options=options)

def get_token_url(url, account):
	driver.get(url)

	# wait up to 10 seconds for the elements to become available
	driver.implicitly_wait(10)

	# use css selectors to grab the login inputs
	email = driver.find_element_by_css_selector('#session_key-oauth2SAuthorizeForm')
	password = driver.find_element_by_css_selector('#session_password-oauth2SAuthorizeForm')
	login = driver.find_element_by_css_selector('input[value="Allow access"]')
	
	email.send_keys(account['email'])
	password.send_keys(account['password'])

	# driver.get_screenshot_as_file('img/main-page.png')

	# login
	login.click()

	driver.implicitly_wait(10)
	# driver.get_screenshot_as_file('img/redirect.png')

	token_url = driver.current_url

	return token_url