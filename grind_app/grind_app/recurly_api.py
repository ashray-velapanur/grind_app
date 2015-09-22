from config import RECURLY
import json
import recurly
from recurly import Account

class RecurlyAPI(object):
	def __init__(self, config=RECURLY):
		recurly.SUBDOMAIN = RECURLY['subdomain']
		recurly.API_KEY = RECURLY['api_key']
		recurly.DEFAULT_CURRENCY = RECURLY['default_currency']

	def get_accounts(self):
		accounts = []
		for account in Account.all():
			acct = {}
			acct['email'] = account.email
			acct['first_name'] = account.first_name
			acct['last_name'] = account.last_name
			acct['company_name'] = account.company_name
			accounts.append(acct)
		return {'Accounts': accounts}