from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
# set the window size
options.add_argument('window-size=1200x600')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

def get_token_url(url, account):
	driver.get(url)

	# wait up to 10 seconds for the elements to become available
	driver.implicitly_wait(10)

	# use css selectors to grab the login inputs
	email = driver.find_element_by_css_selector('#session_key-oauth2SAuthorizeForm')
	password = driver.find_element_by_css_selector('#session_password-oauth2SAuthorizeForm')
	login = driver.find_element_by_css_selector('input[value="Allow access"]')
	
	# print(login)
	email.send_keys(account['email'])
	password.send_keys(account['password'])

	driver.get_screenshot_as_file('img/main-page.png')

	# login
	login.click()

	driver.implicitly_wait(10)
	driver.get_screenshot_as_file('img/redirect.png')

	token_url = driver.current_url

	return token_url

# # navigate to my profile
# driver.get('https://www.facebook.com/profile.php?id=100009447446864')

# # take another screenshot
# driver.get_screenshot_as_file('img/evan-profile.png')

# posts = driver.find_elements_by_css_selector('#stream_pagelet.fbUserContent')
# for post in posts:
#     try:
#         author = post.find_elements_by_css_selector('a[data-hovercard*=user]')[-1].get_attribute('innerHTML')
#         content = post.find_elements_by_css_selector('div.userContent')[-1].get_attribute('innerHTML')
#     except IndexError:
#         # it's an advertisement
#         pass
#     print(f'{author}: "{content}"')