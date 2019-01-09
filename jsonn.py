from requests_oauthlib import OAuth1
import requests
import json

def rqtt(url, plus):
	auth = OAuth1("PvzeEvDvTXhyRtPxFXFCSOx4U","nix6GtK0Q4HS67BKZHu0VyytMJY6Ecue84t8gEMIqGGotgoVZt","1081910144391368704-LpBgTAo33rIpBT94e0SEr62NLkhGBU","AaRIIJ2KcvhB2j23SP3UybabQ8ZzL4pAAUJAaTIkbwP6z")
	try:
		r = requests.get(url + plus, auth=auth)
	except Exception as e:
		print (e)
	r.encoding = 'ISO-8859-1'
	return (r)

def check_usr_cerf(usr):
	try:
		url = "https://api.twitter.com/1.1/users/show.json?screen_name="
		r = rqtt(url, usr)
		stt = r.json().get("verified")
		return (stt)
	except Exception as e:
		print (e)
	return (False)

def read_json(name):
	with open(name, encoding='utf-8') as data_file:
		data = json.loads(data_file.read())
	return (data)

def save_new_json(name, value):
	with open(name, 'w', encoding='utf8') as outfile:
		json.dump(value, outfile)

def main():
	data = read_json("json.json")
	lst_cerf = []
	for name in data['user']:
		print (name)
		if check_usr_cerf(name):
			print ("	" + name)
			lst_cerf.append(name)
			data['user'].remove(name)
	data['user_cerf'] = lst_cerf
	save_new_json("json2.json", data)

main()