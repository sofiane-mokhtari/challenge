import requests
import sys
from requests_oauthlib import OAuth1

def rqtt(url, plus):
	auth = OAuth1("PvzeEvDvTXhyRtPxFXFCSOx4U","nix6GtK0Q4HS67BKZHu0VyytMJY6Ecue84t8gEMIqGGotgoVZt","1081910144391368704-LpBgTAo33rIpBT94e0SEr62NLkhGBU","AaRIIJ2KcvhB2j23SP3UybabQ8ZzL4pAAUJAaTIkbwP6z")
	try:
		r = requests.get(url + plus, auth=auth)
	except Exception as e:
		print (e)
	r.encoding = 'ISO-8859-1'
	return (r)

def check_usr_exist(usr):
	url = "https://api.twitter.com/1.1/users/show.json?screen_name="
	r = rqtt(url, usr)
	stt = r.json().get('errors')
	if stt == None:
		return (True)
	return (False)

def check_usr_cerf(usr):
	try:
		url = "https://api.twitter.com/1.1/users/show.json?screen_name="
		r = rqtt(url, usr)
		stt = r.json().get("verified")
		return (stt)
	except Exception as e:
		pass
	return (False)

print (check_usr_exist(sys.argv[1]))
print (check_usr_cerf(sys.argv[1]))