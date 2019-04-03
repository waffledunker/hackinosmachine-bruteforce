#!/usr/bin/env python
import time
import requests
import hashlib
import sys
import argparse

#parser 

parser = argparse.ArgumentParser()
parser.add_argument('-fn', dest='filename', help= 'filename to pass for hashing')
args = parser.parse_args()

filename = args.filename

print "Passed Argument is " + filename


#argument check
if len(sys.argv) < 2 | len(sys.argv) > 2:
	print "ERROR!!"
	print "Usage : ./foo argument"
	exit()
elif len(sys.argv) == 2:
	print "\nStarting...\n"

#request the page and check if it exists
req = requests.get('http://localhost:8000/')
print "\n Status Code : " + str(req.status_code)

#list of 1-100 numbers
rand_numbers = [i for i in range(1,101)]



#hashmd5 of the string
md5hash = hashlib.md5()


#create new directory with hash and loop over rand_numbers

for i in rand_numbers:
	target_dir = str(filename) + str(i)
	md5hash.update(target_dir)
	new_target = md5hash.hexdigest()
	print "\n" + str(new_target) + "-GENERATED"
	req2 = requests.get('http://localhost:8000/uploads/' + str(new_target))
	if req2.status_code == 200:
		print "SUCCESS!!"
		print "The address of the uploaded file is: " + "/" + str(new_target)
		break
	else:
		print "FAIL! No matches found"

print "Exiting..."
time.sleep(2)
