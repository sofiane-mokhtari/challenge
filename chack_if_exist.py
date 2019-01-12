import requests
import sys, re
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

def get_tweets_by_usr(usr):
	try:
		url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="
		requette = rqtt(url, usr + "&tweet_mode=extended")
		json_ret = requette.json()
		return (json_ret)
	except Exception as e:
		print (e)

def find_hast(tweet):
	return (re.findall("#([A-Za-z0-9_]+)", tweet))

def count_in_list(lst):
	count = {} 
	for ii in lst: 
		if (ii in count): 
			count[ii] += 1
		else: 
			count[ii] = 1
	count = sorted(count.items(),reverse=True, key=lambda t: t[1])
	return (count)

def get_usr_info(usr):
	tweets = get_tweets_by_usr(usr)
	text = []
	if type(tweets) == list:
		for i in tweets:
			text += find_hast(i.get("full_text"))
	info = {'name' : usr, 'hastag' : count_in_list(text)}
	return (info)

a = get_usr_info("MENASTREAM")
print (a)

