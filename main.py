#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pathlib import Path
import time
import datetime
from sel.utils import log_file, driver

from oauth2Linkedin import get_url, get_token
from postLinkedIn import publish_text_on_profile, spaces, publish_content_on_profile
from sel.groupseleniumLinkedin import post_to_group
from sel.seleniumLinkedin import get_token_url
from sel.connectSeleniumLinkedin import connect


def write_to_file(account_data):
	tokens_file = Path('tokens_accounts.json')

	if not tokens_file.is_file():
		with open('tokens_accounts.json', mode='w', encoding='utf-8') as f:
		    json.dump([], f)

	with open('tokens_accounts.json', 'w') as outfile:
		json.dump(account_data, outfile)


def get_old_accounts(option):
	tokens_file = Path('tokens_accounts.json')
	if not tokens_file.is_file():
		return print("ERROR: no such file", tokens_file)

	tokens_file = json.load(open('tokens_accounts.json'))

	for token in tokens_file:
		if(time.time() < token['token']['expires_at']):
			if (option == 'text'):
				post_text = input('Enter post text for account {}: '.format(token['email']))
				publish_text_on_profile(token['token']['access_token'], post_text)
			elif (option == 'content'):
				print('Enter post content for -----{}-----: '.format(token['email']))
				publish_content_on_profile(token['token']['access_token'])
		else:
			print(token['email'],"The token has exprired!")


def get_new_accounts(option):
	accounts = json.load(open('accounts.json'))
	access_url = get_url()
	
	data = []
	
	for account in accounts:
		token_url = get_token_url(access_url, account)
		token = get_token(token_url)

		if (option == 'text'):
			post_text = input('Enter post text for account {}: '.format(account['email']))
			publish_text_on_profile(token['access_token'], post_text)
		elif (option == 'content'):
			print('Enter post content for -----{}-----: '.format(account['email']))
			publish_content_on_profile(token['access_token'])

		account_data = {}
		account_data['email'] = account['email']
		account_data['token'] = token
		data.append(account_data)
	
	write_to_file(data)


while True:
    print(
        '''
        >>> 0 - Exit

        >>> 1 - Use NEW list of accounts post text
        >>> 2 - Use OLD list of accounts post text

        >>> 3 - Use NEW list of accounts post content
        >>> 4 - Use OLD list of accounts post content

        >>> 5 - Post to a group

        >>> 6 - Connect to accounts from xlx file
        '''
    )

    op = input('Enter option: ')

    func = {
        '1': get_new_accounts,
        '2': get_old_accounts,
        '3': get_new_accounts,
        '4': get_old_accounts,
        '5': post_to_group,
        '6': connect,
    }

    if op not in func.keys():
        exit()

    try:
        if op == '1' or op == '2':
            func[op]('text')
        elif op == '3' or op == '4':
            func[op]('content')
        else:
        	func[op]()
    except Exception as ex:
        log_file("ERROR", format(ex))
        driver.get_screenshot_as_file('img/ERROR.png')
        spaces(2)
        print('Error: {}'.format(ex))
