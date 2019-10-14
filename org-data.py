import csv
import json
import string

import pprint

from random import randint

hospital_data = None
addresses_data = None

with open('./Data/hospital-data.csv', 'r') as hospital_data_file:
    hospital_data_reader = csv.DictReader(hospital_data_file)
    hospital_data = [dict(data) for data in hospital_data_reader]

with open('./Data/addresses-us-all.json', 'r') as addresses_data_file:
    addresses_data = json.load(addresses_data_file)['addresses']

speciality = string.ascii_uppercase

hospital_data_len = len(hospital_data)
addresses_data_len = len(addresses_data)
speciality_len = len(speciality)

rand_hos = lambda : hospital_data[randint(0, hospital_data_len - 1)]
rand_add = lambda : addresses_data[randint(0, addresses_data_len - 1)]
rand_spe = lambda : speciality[randint(0, speciality_len - 1)]

records = list()

# n, a, s = rand_hos(), rand_add(), rand_spe()


for _ in range(10000):
    n, a, s = rand_hos(), rand_add(), rand_spe()
    record = {
        'name': n['Hospital Name'],
        'speciality': s,
        'address1': a['address1'],
        'city': a.get('city', ''),
        'state': a['state'],
        'zip': a['postalCode'],
        'coordinates': a['coordinates']
    }
    records.append(record)
    continue

pprint.pprint(records[0:3])

with open('./Data/providers-10000.json', 'w') as fp:
    json.dump(obj=records, fp=fp)
