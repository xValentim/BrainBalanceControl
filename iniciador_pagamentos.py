from json import *
import requests

link = 'https://challenge.hackathonbtg.com/accounts/v1/accounts/:accountId/balances'
headers_parametros = {"organizationId": "69665991-da55-4aac-a1f2-32d23daba8fe", "customerid": "595.080.896-84"}

requestURL = requests.get(url = link, headers = headers_parametros).json()