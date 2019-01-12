from definition import *

def find_by_usr(usr):
	ret = {"user" : [], "hastag" : []}
	json_ret = get_tweets_by_usr(usr)
	if json_ret != None:
		for row in json_ret:
			if (type(row) == dict):
				lst_hastag = find_hast(row.get("full_text"))
				lst_usr = find_usr(row.get("full_text"))
				if lst_hastag != None:
					for value in lst_hastag:
						ret['hastag'].append(value)
				if lst_usr != None:
					for value in lst_usr:
						ret['user'].append(value)
		return ret
	else:
		print ("find_user_error")

def find_by_hast(hastag):
	ret = {"user" : [], "hastag" : []}
	json_ret = get_tweets_by_hastag(hastag)
	if json_ret != None:
		for row in json_ret:
			if (type(row) == dict):
				lst_hastag = find_hast(row.get("full_text"))
				lst_usr = find_usr(row.get("full_text"))
				if lst_hastag != None:
					for value in lst_hastag:
						ret['hastag'].append(hastag)
				if lst_usr != None:
					lst_usr.append(row.get("user").get("screen_name"))
					for value in lst_usr:
						ret['user'].append(value)
		return ret
	else:
		print ("find_hast_error")

def module_de_recherche_by_user(start):
	tmp = find_by_usr(start.name)
	if (tmp == None):
		print("Rien Trouvé")
		return
	#tmp = filtre_lst(tmp)
	start.do_node_user_user(start.name, tmp.get("user"))
	start.do_node_user_hast(start.name, tmp.get("hastag"))
	for value in start.node_user_user.ret:
		tmp = find_by_usr(value)
		if (tmp != None):
			#tmp = filtre_user(tmp)
			start.do_node_user_user(value, tmp.get("user"))
			start.do_node_user_hast(value, tmp.get("hastag"))
	for value in start.node_user_hast.ret:
		tmp = find_by_hast(value)
		if (tmp != None):
			#tmp = filtre_hastag(tmp)
			start.do_node_hast_user(value, tmp.get("user"))
			start.do_node_hast_hast(value, tmp.get("hastag"))



def main():
	start = Tlist(sys.argv[1], None, 0)
	module_de_recherche_by_user(start)
	save_json("json_" + sys.argv[1] + "13_50_12_01_19.json", start.get_json())
	# save("csv_" + sys.argv[1] + ".csv", lst_to_csv(start))

main()