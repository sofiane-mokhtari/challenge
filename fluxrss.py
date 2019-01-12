import requests, re

def get_txt_from_site():
	tout = []
	response = requests.get('https://www.journaldumali.com/feed/')
	for txt in re.findall("(<p>)(.+)(<\/p>)", response.text):
		tout.append(txt[1])
	return (tout)