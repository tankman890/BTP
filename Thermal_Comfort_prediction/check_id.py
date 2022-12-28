import requests
import json

def check_local(id):
	fi = open('permanent_codes.txt', 'r')
	for code in fi:
		if code[-1] == '\n':
			code = code[:-1]
		
		if code == str(id):
			return True

	fi.close()

	return False

def check_remote(id):
	response = requests.get(f"https://BTP.pranavraj14.repl.co")
	id_list = json.loads(response.json())
	for s in id_list:
		if str(id) == s:
			return True
	return False


