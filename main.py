import csv
import instaloader
import datetime import datetime
import os

cmd = input("What would you like to do?  \n \'unfollow\' or \'follow\' or \'update_prospects\' \n --> ")

old_prospects_path = "old_prosepcts.csv"
current_prospect_path = "current_prospects.csv"
future_prospect_path = "current_prospects.csv"

unfollow_period = 3 #days
action_batch_size = 100

prospect_source_accounts = ["medicalertca", "dothealthhq"]


def remove_known_prospects(file_name, name_list):

	del_marks = []

	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file)
	
		for prospect in name_list:

			for person in csv_reader:

				if person[0] == prospect:
					del_marks.append(prospect)

	for person in del_marks:
		name_list.remove(person)

def save_over_file(file_name, new_data):

	os.remove(file_name):

	with open(file_name) as csv_data:

		file_writer = csv.writer(file_name)

		for line in new_data:
			file_writer.writerow(line)

if  cmd == "unfollow":
	return_ar = []

	with open(current_prospect_path) as csv_file:
		csv_reader = csv.reader(csv_file)

		for person in csv_reader:

				if datetime.datetime.today().day - person[1] >= unfollow_period:
					return_ar.append(person[0])

	for person in return_ar:
		input(f"Unfollow -->  {person}  <--")

elif cmd == "follow":

	return_ar = []

	with open(prospect_path) as csv_file:

		csv_reader = csv.reader(csv_file)

		for person in csv_reader:
			if person[2] ==

elif cmd == "update_prospects"

	new_prospects = []

	for account in prospect_source_accounts:
		
		profile = instaloader.Profile.from_username(L.context, account)

		for follower in profile.get_followers():

			if follower not in new_prospects:
				new_prospects.append(follower)
	
	remove_known_prospects(completed_prospects_path, new_prospects)
	remove_known_prospects(prospect_path, new_prospects)

	tmp_ar = new_prospects

	new_prospects = []

	for prospect in temp_ar:
		
		_ = []

		_.append(prospect)
		_.append(datetime.datetime.today().day)
		_.append("prospect")

		new_prospects.append(_)
	
