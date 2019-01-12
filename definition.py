import requests
import re, sys, json
from requests_oauthlib import OAuth1

class Tlist():

	def __init__(self, name, lst, t):
		self.name = name
		self.prev = None
		self.type = t
		self.add_lst(lst)
		self.node_user_user = None
		self.node_user_hast = None
		self.node_hast_user = None
		self.node_hast_hast = None
		self.next = None

	def get_json(self):
		ret = [{}]
		i = 0
		tmp = self
		while (tmp):
			ret[i]["name"] = tmp.name
			ret[i]["type"] = tmp.type
			ret[i]["list_user"] = tmp.ret
			ret[i]["nombre_user"] = tmp.len_ret
			if (tmp.node_user_user != None):
				ret[i]["node_user_user"] = tmp.node_user_user.get_json()
			if (tmp.node_user_user != None):
				ret[i]["node_user_hast"] = tmp.node_user_hast.get_json()
			if (tmp.node_user_user != None):
				ret[i]["node_hast_user"] = tmp.node_hast_user.get_json()
			if (tmp.node_user_user != None):
				ret[i]["node_hast_hast"] = tmp.node_hast_hast.get_json()
			i += 1
			tmp = tmp.next
		return ret

	def add_next(self, value):
		tmp = self.get_end()
		tmp.next = value
		value.prev = tmp

	def add_lst(self, value):
		self.ret = value
		self.len_ret = len(value) if value else 0

	def get_start(self):
		if (self.prev == None):
			return self
		return self.prev.get_start()

	def get_begin(self):
		if (self.node == None):
			return self
		return self.node.get_begin()

	def del_one(self):
		if (self.next == None and self.prev == None):
			return None
		if (self.prev == None):
			self.next.prev = None
			return self.next
		if (self.next == None):
			self.prev.next == None
			return None
		self.next.prev = self.prev
		self.prev.next = self.next
		return self.next

	def get_end(self):
		if (self.next == None):
			return self
		return self.next.get_end()

	def do_node_user_user(self, value, lst):
		if (self.node_user_user == None):
			self.node_user_user = Tlist(value, lst, 1)
		else:
			self.node_user_user.add_next(Tlist(value, lst, 1))

	def do_node_user_hast(self, value, lst):
		if (self.node_user_hast == None):
			self.node_user_hast = Tlist(value, lst, 2)
		else:
			self.node_user_hast.add_next(Tlist(value, lst, 2))

	def do_node_hast_user(self, value, lst):
		if (self.node_hast_user == None):
			self.node_hast_user = Tlist(value, lst, 1)
		else:
			self.node_hast_user.add_next(Tlist(value, lst, 1))

	def do_node_hast_hast(self, value, lst):
		if (self.node_hast_hats == None):
			self.node_hast_hast = Tlist(value, lst, 2)
		else:
			self.node_hast_hast.add_next(Tlist(value, lst, 2))

def read_json(name):
	with open(name, encoding='utf-8') as data_file:
		data = json.loads(data_file.read())
	return (data)

def save_new_json(name, value):
	with open(name, 'w', encoding='utf8') as outfile:
		json.dump(value, outfile)

def save_json(path, di):
	jsonn = json.dumps(di)
	f = open(path,"w")
	f.write(jsonn)
	f.close()

def save(path, txt):
	fichier = open(path, "w")
	fichier.write(txt)
	fichier.close()

def supprimer_dooublon(lst):
	for key,value in lst:
		while (lst.count() > 1):
			lst.remove(value)
	return (lst)

def count_in_list(lst):  
	count = {} 
	for ii in lst: 
		if (ii in count): 
			count[ii] += 1
		else: 
			count[ii] = 1
	count = sorted(count.items(),reverse=True, key=lambda t: t[1])
	return (count)

def rqtt(url, plus):
	auth = OAuth1("PvzeEvDvTXhyRtPxFXFCSOx4U","nix6GtK0Q4HS67BKZHu0VyytMJY6Ecue84t8gEMIqGGotgoVZt","1081910144391368704-LpBgTAo33rIpBT94e0SEr62NLkhGBU","AaRIIJ2KcvhB2j23SP3UybabQ8ZzL4pAAUJAaTIkbwP6z")
	try:
		r = requests.get(url + plus, auth=auth)
	except Exception as e:
		print("rqttt")
		print (e)
	r.encoding = 'ISO-8859-1'
	return (r)

def get_tweets_by_hastag(hastag):
	try:
		url = "https://api.twitter.com/1.1/search/tweets.json?q="
		requette = rqtt(url, "%23" + hastag  + "&tweet_mode=extended")
		json_ret = requette.json().get("statuses")
		return (json_ret)
	except Exception as e:
		print ("get_tweets_by_hast")
		print (e)

def get_tweets_by_hastag_if_count(hastag):
	try:
		url = "https://api.twitter.com/1.1/search/tweets.json?q="
		requette = rqtt(url, "%23" + hastag  + "&tweet_mode=extended")
		json_ret = requette.json()
		return (json_ret)
	except Exception as e:
		print (e)

def get_usr_info(usr):
	tweets = get_tweets_by_usr(usr)
	text = []
	if type(tweets) == list:
		for i in tweets:
			text += find_hast(i.get("full_text"))
	info = {'name' : usr, 'hastag' : count_in_list(text)}
	return (info)

def get_tweets_by_usr(usr):
	try:
		url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="
		requette = rqtt(url, "%40" + usr + "&tweet_mode=extended")
		json_ret = requette.json()
		return (json_ret)
	except Exception as e:
		print ("get_tweets_by_usr")
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
	if tweet == None:
		return None
	try:
		ret = re.findall("#([A-Za-z0-9_]+)", tweet)
		# ret = supprimer_dooublon(ret)
	except Exception as e:
		print ("find hast")
		print (e)
		print (tweet)
	return (ret)

def find_usr(tweet):
	if tweet == None:
		return None
	try:
		ret = re.findall("@([A-Za-z0-9_]+)", tweet)
		#ret = supprimer_dooublon(ret)
	except Exception as e:
		print ("find user")
		print (e)
		print (tweet)
	return (ret)

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

def put_without_double(lst_dst, lst_src):
	lst_double = []
	for i in lst_src:
		if i not in lst_dst:
			lst_double.append(i)
	return (lst_double)

def filtre_hastag(lst_hastag):
	return True


def filtre_user(lst_user):
	return True
