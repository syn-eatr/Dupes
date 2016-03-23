#! /usr/local/bin/python3

import os
import re
import hashlib

tFolderList = []


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
			
			if md5h not in md5dict:
				md5dict[md5h] = []

			md5dict[md5h].append(result)


	if not md5dict:
		print('\nSource directory not available: ' + path + '\n')
	else:
		print(" Directory: " + str(len(md5dict)) + " unique files")	
	
	return md5dict

# TV Folder capture

unique_md5 = folder_capture(tPath)
				
print("")
 

for unique in unique_md5:
	for unique_dir in range(0, len(unique_md5[unique])):
		if len(unique_md5[unique]) >= 2:
			if unique_dir == 0:
				print("")
			print(unique + ': ' + unique_md5[unique][unique_dir])

print("")
