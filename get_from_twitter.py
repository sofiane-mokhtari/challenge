import requests
import re
from requests_oauthlib import OAuth1
import json

tout = {'hastag' : [], 'user' : []}
 
def save_json(path, di):
	jsonn = json.dumps(di)
	f = open(path,"w")
	f.write(jsonn)
	f.close()

def rqtt(url, plus):
	auth = OAuth1("PvzeEvDvTXhyRtPxFXFCSOx4U","nix6GtK0Q4HS67BKZHu0VyytMJY6Ecue84t8gEMIqGGotgoVZt","1081910144391368704-LpBgTAo33rIpBT94e0SEr62NLkhGBU","AaRIIJ2KcvhB2j23SP3UybabQ8ZzL4pAAUJAaTIkbwP6z")
	try:
		r = requests.get(url + plus, auth=auth)
	except Exception as e:
		print (e)
	r.encoding = 'ISO-8859-1'
	return (r)

def get_tweets_by_hastag(hastag):
	try:
		url = "https://api.twitter.com/1.1/search/tweets.json?q="
		requette = rqtt(url, "%23" + hastag)
		json_ret = requette.json().get("statuses")
		return (json_ret)
	except Exception as e:
		print (e)
	

def get_tweets_by_usr(usr):
	try:
		url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="
		requette = rqtt(url, usr)
		json_ret = requette.json()
		return (json_ret)
	except Exception as e:
		print (e)

def get_follow_by_usr(usr):
	try:
		url = "https://api.twitter.com/1.1/followers/list.json?screen_name="
		requette = rqtt(url, usr)
		json_ret = requette.json()
	except Exception as e:
		print (e)
	return (json_ret)

def find_hast(tweet):
	return (re.findall("#([A-Za-z0-9_]+)", tweet))

def find_usr(tweet):
	return (re.findall("@([A-Za-z0-9_]+)", tweet))

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

def save(path, txt):
	fichier = open(path, "w")
	fichier.write(txt)
	fichier.close()

def supprimer_dooublon(lst):
	for key,value in lst:
		while (lst.count() > 1):
			lst.remove(value)
	return (lst)

def put_without_double(lst_dst, lst_src):
	for i in lst_src:
		if i not in lst_dst:
			lst_dst.append(i)
	return (lst_dst)

def find_by_usr(usr, index, tout):
	if index == 0:
		return
	json_ret = get_tweets_by_usr(usr)
	if json_ret != None:
		for row in json_ret:
			lst_hastag = find_hast(row.get("text"))
			lst_usr = find_usr(row.get("text"))
			tout['hastag'] = put_without_double(tout['hastag'], lst_hastag)
			tout['user'] = put_without_double(tout['user'], lst_usr)
			for value in lst_hastag:
				print ("	hastag =	" + value)
				find_by_hast(value, index - 1, tout)
			for value in lst_usr:
				print ("	usr =		" + value)
				find_by_usr(value, index - 1, tout)
	else:
		print ("fuck")

def find_by_hast(hastag, index, tout):
	if index == 0:
		return
	json_ret = get_tweets_by_hastag(hastag)
	if json_ret != None:
		for row in json_ret:
			lst_hastag = find_hast(row.get("text"))
			lst_usr = find_usr(row.get("text"))
			usr = row.get("user").get("screen_name")
			tout['hastag'] = put_without_double(tout['hastag'], lst_hastag)
			tout['user'] = put_without_double(tout['user'], lst_usr)
			if usr not in tout['user']:
				tout['user'].append(usr)
			for value in lst_hastag:
				print ("	hastag =	" + value)
				find_by_hast(value, index - 1, tout)
			for value in lst_usr:
				print ("	usr =		" + value)
				find_by_usr(value, index - 1, tout)
			find_by_usr(usr, index - 1, tout)
	else:
		print ("fuck")


def main():
	global tout
	hastag = ["Al_Mansour_ag_Alkassim","Amadou_Kouffa","AnsarDine","AnsaroulIslam","AQMI","Azawad","Azawadien","azawadienne","Barkhane","Chamanamass","CMA","CSA","Dawsahak","Dozos","EIGS","FAMA","FAMAs""G5Sahel","GATIA","HCUA","Imghad","ISGS","JNIM","KatibaMacina","KelTamasheq","Koglweogo","Lwili","MAA","Macina","MFA","MINUSMA","MNLA","MOC","MSA","Peuls","Plateforme","Tin_Buktu"]
	for h in hastag:
		print (h)
		find_by_hast(h, 2, tout)
	save_json("json.json", tout)

main()