from definition import *
import sys



def main():
	# save_json("a.json", get_tweets_by_usr(sys.argv[1]))
	ret = {}
	tout_1 = []
	tout_2 = []
	plus_plus = []
	plus_plus_plus = []
	data = read_json(sys.argv[1])
	start = data[0].get("BRANCHE_user_user")[0]
	user = data[0].get("liste_return")[0]
	file = open("csv_" + user + "_" + time.strftime('%X_%x').replace(":", "_").replace("/", "_") + ".csv", "w")
	c = csv.writer(file)
	c.writerow([sys.argv[1], "+++", "++", "1", "2", "3"])
	if start.get("BRANCHE_user_user") != None:
		for node in start.get("BRANCHE_user_user"):
			tmp = node.get("liste_return")
			if user in tmp:
				print (node)
				plus_plus_plus.append(node.get("name"))
			tout_1 += tmp
			if node.get("BRANCHE_user_user") != None:
				for node_2 in node.get("BRANCHE_user_user"):
					tmp_2 = node_2.get("liste_return")
					if user in tmp_2:
						plus_plus.append(node_2.get("name"))
					tout_2 += tmp_2
	tout = start.get("liste_return")
	total = list(set(tout + tout_1 + tout_2))
	print (plus_plus)
	print (plus_plus_plus)
	for value in total:		
		ret[value] = [value, 0, 0, 0, 0, 0]
		if value in plus_plus:
			ret.get(value)[2] += 1
		if value in plus_plus_plus:
			ret.get(value)[1] += 1
	for value in tout:
		if (value != sys.argv[1]):
			ret.get(value)[3] += 1
	for value in tout_1:
		if (value != sys.argv[1]):
			ret.get(value)[4] += 1
	for value in tout_2:
		if (value != sys.argv[1]):
			ret.get(value)[5] += 1
	for value in total:
		# print (ret.get(value))
		c.writerow(ret.get(value))
	file.close()

main()