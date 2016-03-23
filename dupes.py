#! /usr/local/bin/python3

import os
import re
import hashlib

tFolderList = []

totalWasted = []

wasted = {}


tPath = "/Users/villan/Desktop/Python/Queue/"

print("")

def md5hash(fname):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    x = hash.hexdigest()
    return x

def folder_capture(path):

	md5dict = {}

	for root, dirs, files in os.walk(path):
	
		for i in files:
			if ".DS_Store" in i:
				continue

			result = os.path.join(root, i)
			md5h = md5hash(result)
			size = os.stat(result).st_size
			wasted[result] = size
			
			if md5h not in md5dict:
				md5dict[md5h] = []

			md5dict[md5h].append(result)

	if not md5dict:
		print('\nSource directory not available: ' + path + '\n')
	else:
		print(" Directory: " + str(len(md5dict)) + " unique files")	
	
	return md5dict

def slack(passed_hash):
	slack_total = 0

	for i in range(1, len(passed_hash)):
		slack_total += wasted[passed_hash[i]]
		totalWasted.append(slack_total)
		return int(slack_total) / 1024 / 1024

# TV Folder capture

unique_md5 = folder_capture(tPath)
				
print("")
 

for hash_code in unique_md5:
	for unique_dir in range(0, len(unique_md5[hash_code])):
		if len(unique_md5[hash_code]) >= 2:
			if unique_dir == 0:
				print("")

			print(hash_code + ': ' + unique_md5[hash_code][unique_dir])

			if unique_dir == len(unique_md5[hash_code]) - 1:
				print('Wasted Space: ' + str(slack(unique_md5[hash_code])) + 'MB')

print("")

print('Total Waste: ' + str(sum(totalWasted) / 1024 / 1024) + 'MB')
print("")