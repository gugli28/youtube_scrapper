#!/usr/bin/python
import os
import re
from bs4 import BeautifulSoup
# //regex
# find_http = re.compile("^http")
# opening file
fileObject = open("/home/gugli/Documents/script_py/maha.html" ,"r")

soup = BeautifulSoup(fileObject.read())
##finding tag a in the page source
a_tag = soup.find_all("a")

href_list = []
for item in a_tag:
	href_list += [item['href']]
# print href_list

# dir_name = raw_input("dirname ")
# name = "mkdir" + dir_name
os.system("mkdir maha_vid")
os.chdir("/home/gugli/Documents/script_py/maha_vid")
# os.chdir("/home/prince/Documents/documents/scripts_py/others")

os.system("pwd")
count = 1
for line in href_list:
# 	if find_http.search(line):
	url = "https://www.youtube.com"+ line.rstrip()
	# b = "youtube-dl -f 18 " + url
	b = "youtube-dl -f bestvideo+bestaudio " + url

	print "COMMAND " , b,'\n'
	# print url,'\n'
	os.system(b)
	print "Done " , count , '\n',b

print "wubba lubba dub dub"
