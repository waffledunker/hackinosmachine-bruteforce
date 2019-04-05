This is a bruteforce uri directory finder on HackinOs machine that is vulnerable. 

Machine requires from user to find uploaded file by bruteforce.Uploaded file name, basically hashed and placed to that hash value named directory.

Your uploaded file will be in the directory of md5 hashed and random number added version of your filename.

USAGE : ./foo -fn youruploadedfilename.foo

this script will try to connect every combination of random number + hash and will return you directory which is reachable.
