from flask import Flask, Response, make_response, render_template
app = Flask(__name__)

def rqtt(url, plus):
	auth = OAuth1("PvzeEvDvTXhyRtPxFXFCSOx4U","nix6GtK0Q4HS67BKZHu0VyytMJY6Ecue84t8gEMIqGGotgoVZt","1081910144391368704-LpBgTAo33rIpBT94e0SEr62NLkhGBU","AaRIIJ2KcvhB2j23SP3UybabQ8ZzL4pAAUJAaTIkbwP6z")
	try:
		r = requests.get(url + plus, auth=auth)
	except Exception as e:
		print("rqttt")
		print (e)
	r.encoding = 'ISO-8859-1'
	return (r)

def get_tweets_by_usr(usr, nb):
	try:
		url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="
		requette = rqtt(url, "%40" + usr + "&tweet_mode=extended&count=" + nb)
		print (requette)
		json_ret = requette.json()
		return (json_ret)
	except Exception as e:
		if (requette.json().get("errors")[0].get("code") == 88):
			time.sleep(5)
			return get_tweets_by_usr(usr)
		return None

def get_tweets_by_hastag(hastag, nb):
	try:
		url = "https://api.twitter.com/1.1/search/tweets.json?q="
		requette = rqtt(url, "%23" + hastag  + "&tweet_mode=extended&count=" + nb)
		json_ret = requette.json()
		return (json_ret)
	except Exception as e:
		if (requette.json().get("errors")[0].get("code") == 88):
			time.sleep(5)
			return get_tweets_by_hastag(hastag)
		return None

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

def get_user(value, typee, nb):
	if (typee):
		tweets = get_tweets_by_hastag(value, nb)
	else:
		tweets = get_tweets_by_user(value, nb)


@app.route("/")
def get_home():
	render_template("index.html")

@app.route("/tweet_hast/<hastag>")
def get_last_tweet_by_h(hastag):
	ret = {[]}
	json_ret = get_last_tweet_by_h(hastag, 20)
	for tweet in json_ret.get('status'):
		tmp = {}
		tmp['id'] = tweet.id
		tmp['name'] = tweet.user.name
		tmp['screnn_name'] = tweet.user.screen_name
		tmp['date'] = tweet.created_at
		ret.append(tweet.full_text)
	ret['next'] = json_ret.get('search_metadata').refresh_url
	return Response(response=json.dumps(ret), status=200, mimetype='application/json')

@app.route("/tweet_user/<user>")
def get_last_tweet_by_user(user):
	ret = {[]}
	json_ret = get_last_tweet_by_usr(user, 20)
	for tweet in json_ret.get('status'):
		tmp = {}
		tmp['id'] = tweet.id
		tmp['name'] = tweet.user.name
		tmp['screnn_name'] = tweet.user.screen_name
		tmp['date'] = tweet.created_at
		ret.append(tweet.full_text)
	ret['next'] = json_ret.get('search_metadata').refresh_url
	return Response(response=json.dumps(ret), status=200, mimetype='application/json')

@app.route("/relation/<value>/<type>")
def relation(value, typee):
	ret = relation_entre_tweet(value, typee)
	return Response(response=json.dumps(ret.get_json()), status=200, mimetype='application/json')

@app.route("/graph_value/<value>/<type>/<config>")
def graph_value(value, typee, config):
	ret = {}
	json_ret = get_tweets_by_hastag()

@app.route("/carto/<value>/<typee>/<nb>")
def carto(value, typee, nb):
	ret = {[]}
	if (typee):
		user = get_

print (__name__)
if __name__ == '__main__':
	app.run(debug=True)