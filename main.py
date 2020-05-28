import json
import instaloader
import csv
from datetime import datetime
import os

cmd = input("What would you like to do?  \n \'unfollow\' or \'follow\' or \'update\' \n --> ")

old_prospects_path = "old_prospects.csv"
current_prospect_path = "current_prospects.csv"
future_prospect_path = "future_prospects.csv"

unfollow_period = 3 #days
action_batch_size = 100

prospect_source_accounts = ["rileyjacksonx.o"] #"medicalertca", "dothealthhq"]


def remove_known_prospects(file_name, name_list):

	del_marks = []

	with open(file_name, "r") as jsondata:
		jsonreader = json.load(jsondata)
	
		for prospect in name_list:

			for person in list(jsonreader["current"].keys()):
				if prospect == person["user"]

	for person in del_marks:
		name_list.remove(person)

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

	print(new_prospects)
	final_ar = []

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
