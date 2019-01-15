from definition import *
from variable import *

global_variable = Variable()

def find_by_usr(usr):
	if (usr == sys.argv[1]):
		return 
	ret = {"user" : [], "hastag" : []}
	json_ret = get_tweets_by_usr(usr)
	if json_ret != None:
		json_ret = json_ret
		for row in json_ret:
			if (type(row) == dict):
				lst_hastag = find_hast(row.get("full_text"))
				lst_usr = find_usr(row.get("full_text"))
				if lst_hastag != None:
					for value in lst_hastag:
						print ("		hastag = " + value)
						ret['hastag'].append(value)
				if lst_usr != None:
					for value in lst_usr:
							if not check_usr_cerf(value):
								print ("		user = " + value)
								ret['user'].append(value)
		return ret

def find_by_hast(hastag):
	ret = {"user" : [], "hastag" : []}
	json_ret = get_tweets_by_hastag_if_count(hastag)
	if json_ret != None:
		for row in json_ret:
			if (type(row) == dict):
				lst_hastag =find_hast(row.get("full_text"))
				lst_usr = find_usr(row.get("full_text"))
				if lst_hastag != None:
					for value in lst_hastag:
						print ("		hastag = " + value)
						ret['hastag'].append(value)
				if lst_usr != None:
					lst_usr.append(row.get("user").get("screen_name"))
					for value in lst_usr:
							if not check_usr_cerf(value):
								print ("		user = " + value)
								ret['user'].append(value)
		return ret

def module_de_recherche_by_user(start, i):
	if i <= 0:
		return
	print ("user i = " + str(i))
	for value in list(set(start.ret)):
		tmp = find_by_usr(value)
		if (tmp == None):
			print("Rien Trouvé pour l'user " + value)
		else :
			start.do_node_user_user(value, tmp.get("user"))
			start.do_node_user_hast(value, tmp.get("hastag"))
			node = start.node_user_user
			while (node):
				module_de_recherche_by_user(node, i - 1)
				node = node.next
			node = start.node_user_hast
			while (node):
				module_de_recherche_by_hastag(node, i - 1)
				node = node.next
			node = start.node_hast_user
			while (node):
				module_de_recherche_by_user(node, i - 1)
				node = node.next
			node = start.node_hast_hast
			while (node):
				module_de_recherche_by_hastag(node, i - 1)
				node = node.next

def module_de_recherche_by_hastag(start, i):
	if i == 0:
		return
	print ("hastag i = " + str(i))
	for value in list(set(start.ret)):
		tmp = find_by_hast(value)
		if (tmp == None):
			print("Rien Trouvé pour l'hastag " + value)
		else :
			start.do_node_hast_user(value, tmp.get("user"))
			start.do_node_hast_hast(value, tmp.get("hastag"))
			node = start.node_user_user
			while (node):
				module_de_recherche_by_user(node, i - 1)
				node = node.next
			node = start.node_user_hast
			while (node):
				module_de_recherche_by_hastag(node, i - 1)
				node = node.next
			node = start.node_hast_user
			while (node):
				module_de_recherche_by_user(node, i - 1)
				node = node.next
			node = start.node_hast_hast
			while (node):
				module_de_recherche_by_hastag(node, i - 1)
				node = node.next

def relation_entre_tweet(inpuut, i):
	start = Tlist("algo", [inpuut] , 0)
	if (i == 0):
		for value in start.ret:
			tmp = find_by_usr_special(value)
			print (tmp)
			if (tmp == None):
				print("Rien Trouvé pour l'user " + value)
			else :
				start.do_node_user_user(value, tmp.get("user"))
				start.do_node_user_hast(value, tmp.get("hastag"))
				node = start.node_user_user
				while (node):
					module_de_recherche_by_user(node, 2)
					node = node.next
				node = start.node_user_hast
				while (node):
					module_de_recherche_by_hastag(node, 2)
					node = node.next
				node = start.node_hast_user
				while (node):
					module_de_recherche_by_user(node, 2)
					node = node.next
				node = start.node_hast_hast
				while (node):
					module_de_recherche_by_hastag(node, 2)
					node = node.next
	else:
		for value in start.ret:
			tmp = find_by_hast(value)
			print (tmp)
			if (tmp == None):
				print("Rien Trouvé pour l'user " + value)
			else :
				start.do_node_hast_user(value, tmp.get("user"))
				start.do_node_hast_hast(value, tmp.get("hastag"))
				node = start.node_user_user
				while (node):
					module_de_recherche_by_user(node, 2)
					node = node.next
				node = start.node_user_hast
				while (node):
					module_de_recherche_by_hastag(node, 2)
					node = node.next
				node = start.node_hast_user
				while (node):
					module_de_recherche_by_user(node, 2)
					node = node.next
				node = start.node_hast_hast
				while (node):
					module_de_recherche_by_hastag(node, 2)
					node = node.next
	return (start)

def main():
	start = relation_entre_tweet(sys.argv[1], sys.argv[2])
	# start.get_csv_by_relation("csv2_" + lst[0])
	print ("FILE NAME")
	print ("json_new" + sys.argv[1] + "_" + time.strftime('%X_%x').replace(":", "_") + ".json")
	save_json("json_new" + sys.argv[1] + "_" + time.strftime('%X_%x').replace(":", "_") + ".json", start.get_json())
	# save("csv_" + sys.argv[1] + ".csv", lst_to_csv(start))

main()