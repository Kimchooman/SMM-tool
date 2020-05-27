import json
import instaloader
import csv
from datetime import datetime
import os

cmd = input("What would you like to do?  \n \'unfollow\' or \'follow\' or \'update\' \n --> ")

prospect_file_path =  "prospects.json"

unfollow_period = 3 #days
action_batch_size = 100

prospect_source_accounts = ["rileyjacksonx.o"] #"medicalertca", "dothealthhq"]


def remove_known_prospects(file_name, name_list):

	del_marks = []

	with open(file_name) as json_file:
		data = json.load(csv_file)
	
		for prospect in name_list:
			
			try:
				try:
					try:
						data["current"][prospect]
						del_marks.append(prospect)

					except:
						data["future"][prospect]
						del_marks.append(prospect)
			
				except:
					data["past"][prospect]
					del_marks.append(prospect)
			
			except:
				pass
	
	for mark in del_marks:
		
		data["current"].pop(mark, None)
		data["past"].pop(mark, None)
		data["future"].pop(mark, None)

def save_over_file(file_name, new_data):

	os.remove(file_name)

	with open(file_name) as csv_data:

		file_writer = csv.writer(file_name)

		for line in new_data:
			file_writer.writerow(line)

if  cmd == "unfollow":
	return_ar = []

	with open(current_prospect_path) as csv_file:
		csv_reader = csv.reader(csv_file)

		count = 0
		for person in csv_reader:

				if count < action_batch_size:
					if datetime.datetime.today().day - person[1] >= unfollow_period:
					
						count += 1
						return_ar.append(person)

	with open(old_prospects_path) as csv_file:
		
		csv_writer = csv.writer(csv_file)

		for person in return_ar:
			input(f"Unfollow -->  {person[0]}  <--")
			csv_writer.writeline(person)
		
	for person in return_ar:
		csv_reader.remove(person)

		save_over_file(current_prospect_path, csv_reader)

elif cmd == "follow":

	working_ar = []

	with open(future_prospect_path) as csv_file:

		csv_reader = csv.reader(csv_file)

		count = 0

		for person in csv_reader:
			if count < action_batch_size:
				
				working_ar.append(person)
				count += 1 

			else:
				break
		
	for person in working_ar:
		csv_reader.remove(person)

	save_over_file(future_prospect_path, csv_reader)

	with open(current_prospect_path) as csv_file:

		for person in working_ar:

			input(f"Follow -->  {person[0]}  <--")
			csv_writer.writeline(person)

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
				new_prospects.append(follower.username)
	
	remove_known_prospects(old_prospects_path, new_prospects)
	remove_known_prospects(current_prospect_path, new_prospects)
	remove_known_prospects(future_prospect_path, new_prospects)
	

	for prospect in new_prospects:
		
		_ = []

		_.append(prospect)
		_.append(datetime.today().day)

		final_ar.append(_)
	
	with open(future_prospect_path) as csv_file:

		csv_writer = csv.writer(csv_file)

		for line in final_ar:
			print(line)
			csv_writer.writerow(line)
