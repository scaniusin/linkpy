from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix

# Credentials you get from registering a new application
client_id = '86wvkev2onheqr'
client_secret = 'TpYJ7sD48tetkTbt'

# OAuth endpoints given in the LinkedIn API documentation
authorization_base_url = 'https://www.linkedin.com/uas/oauth2/authorization'
token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'

linkedin = OAuth2Session(client_id, redirect_uri='https://127.0.0.1:8000')
linkedin = linkedin_compliance_fix(linkedin)

def get_url():
	# Redirect user to LinkedIn for authorization
	authorization_url, state = linkedin.authorization_url(authorization_base_url)
	return authorization_url

def get_token(redirect_response):
	# Fetch the access token
	token = linkedin.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)
	return token
