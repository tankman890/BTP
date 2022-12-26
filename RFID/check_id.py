import requests
import json

def check(id):
	response = requests.get(f"https://BTP.pranavraj14.repl.co")
	id_list = json.loads(response.json())
	for s in id_list:
		if str(id) == s:
			return True
	return False


check("hi")
