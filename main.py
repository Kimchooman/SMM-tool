import json
import instaloader
from datetime import datetime
import subprocess
import random

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def delta_days(date: list):
	months = date[0]
	days = date[1]

	c_day = datetime.today().days
	c_month = datetime.today().month
	
	d_day = c_day - days
	d_month = c_month - months

	return d_days + (d_months * 30)

cmd = input("What would you like to do?  \n \'unfollow\' or \'follow\' or \'update\' \n --> ")

prospect_path = "prospects.json"

unfollow_period = 3 #days
action_batch_size = 100

prospect_source_accounts = ["immanueljones8"]#"medicalertca", "dothealthhq"]

if  cmd == "unfollow":
	
	with open(prospect_path, "r") as json_file:
		data = json.load(json_file)

		current_people = data["current"].keys()

		count = 0
		for target in current_people:

			copy2clip(target)

			input(f"unfollow -->  {target}  <--")

			temp_holder = data["current"][target]
			data["current"].pop(target)
			data["past"][target] = temp_holder

			with open(prospect_path, "w") as json_file:

				json.dump(data, json_file)
			if count >= action_batch_size:
				break
			
			count += 1
		


elif cmd == "follow":

	with open(prospect_path, "r") as json_file:
		data = json.load(json_file)

	count = 0

	future_prospects = list(data["future"].keys())
	
	del_marks = []

	for person in future_prospects:

		copy2clip(person)
		input(f"\nFollow -->  {person}  <--\n")

		temp_holder = data["future"][person]

		data["future"].pop(person, None)

		data["current"][person] = temp_holder

		with open(prospect_path, "w") as json_file:
			json.dump(data, json_file)
		
		count += 1

		if count >= action_batch_size:
			break
	
elif cmd == "RESET":

	num = random.randint(1,100)
		
	if input(f"Type: {num}  -->") == num:
		with open(prospect_path, "w") as json_file:

			save = {"current": {},"past": {},"future": {}}

			json.dump(save, json_file)

elif cmd == "update":

	new_prospects = []
	
	L = instaloader.Instaloader()
	L.login("l1b0j2", "mouseking") 

	for account in prospect_source_accounts:
		
		profile = instaloader.Profile.from_username(L.context, account)
		
		for follower in profile.get_followers():
			for prospect in new_prospects:

				if prospect == follower:
					break
				
			else:
				new_prospects.append(follower)
	
	
	with open(prospect_path, "r") as json_file:

		data = json.load(json_file)
		#data = json.loads(data)

		for prospect in new_prospects:

			try:
				try:
					try:
						data["current"][prospect.username]
						new_prospects.remove(prospect)

					except:
						data["future"][prospect.username]
						new_prospects.remove(prospect)
				
				except:
					data["past"][prospect.username]
					new_prospects.remove(prospect)

			except:

				data["future"][prospect.username] = {}
				data["future"][prospect.username]["know_since"] = [datetime.today().month, datetime.today().day, datetime.today().year]
				data["future"][prospect.username]["is_business"] = prospect.is_business_account


	with open(prospect_path, "w") as jsonfile:

		json.dump(data, jsonfile)
