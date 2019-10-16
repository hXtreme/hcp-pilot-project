import csv
import json

import pprint

def to_csv(json_file, csv_file):
	records = [
		['name', 'speciality', 'address1', 'city', 'state', 'zip', 'lat', 'lng']
	]
	with open(json_file, 'r') as json_fp:
		for data in json.load(json_fp):
			record = [
				data['name'], 
				data['speciality'], 
				data['address1'], 
				data['city'], 
				data['state'], 
				data['zip'], 
				data['coordinates']['lat'], data['coordinates']['lng']
			]
			records.append(record)
	with open(csv_file, 'w') as fp:
		for record in records:
			print(record)
			print(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], sep=', ', file=fp, flush=True)
	pass


def to_json(csv_file, json_file):
	records = list()
	with open(csv_file, 'r') as csv_fp:
		data_reader = csv.DictReader(csv_fp)
		for data in data_reader:
			record = {
				'name': data['name'],
				'speciality': data['speciality'],
				'address1': data['address1'],
				'city': data.get('city', ''),
				'state': data['state'],
				'zip': data['zip'],
				'coordinates': {
					'lat': data['lat'], 
					'lng': data['lng']
					}
			}
			records.append(record)
	with open(json_file, 'w') as fp:
		json.dump(obj=records, fp=fp)
	pass

def ask(option=None, json_file=None, csv_file=None):
	if option == None: option = input('To Json: J\nTo CSV: C')
	if json_file == None: json_file = input('Json filepath: ')
	if csv_file == None: csv_file = input('CSV filepath: ')
	if option == 'J':
		to_json(csv_file, json_file)
	elif option == 'C':
		to_csv(json_file, csv_file)
	print('Done!')

OPTION = 'C'
JSON_FILE = './Data/providers.json'
CSV_FILE = './Data/providers.csv'
ask(OPTION, JSON_FILE, CSV_FILE)
