#!/usr/bin/python
import requests
import time
import json

failed = []#------------{0 to 1100}{1101 to 1900}{1901 to 2100} of 8172---------{0 to 250}{251 to 500} of 8192
emailid = {"OFH0P0" : ["seventhdreamofteenageheaven@gmail.com"], "YLYKXF": ["hinataislovehinataislife247@gmail.com"]}
'''
for theemailid in emailid["YLYKXF"]:
	koid = "YLYKXF"
	email = theemailid[:-10]
	print email
	emailList = []

	def insertDots(str, at):
		if(at == 0):
			emailList.append(str)
			return
		newStr = str[:at] + "." + str[at:]
		for i in xrange(0, at, 2):
			insertDots(newStr, i)

	def allDots(str):
		for i in range(0, len(str), 2):
			insertDots(str,i)


	allDots(email.replace(".", ""))

	print len(emailList)

	i = 1

	for mail in emailList[251:500]:
		requestURL = "https://invites.oneplus.net/index.php?r=share/signup&success_jsonpCallback=success_jsonpCallback&email={0}@gmail.com&koid={1}&_=1439105125402".format(mail, koid)
		print "Sending invite to  " + mail
		res = requests.get(requestURL)
		if(res.status_code == 200):
			print "Successfully retrieved response"
		else:
			print "Oneplus servers are babies, request failed"
			failed.append(mail)
		print str(i) + "/" + str(len(emailList))
		i = i + 1
		time.sleep(3)
'''
for theemailid in emailid["OFH0P0"]:
	koid = "OFH0P0"
	email = theemailid[:-10]
	print email
	emailList = []

	def insertDots(str, at):
		if(at == 0):
			emailList.append(str)
			return
		newStr = str[:at] + "." + str[at:]
		for i in xrange(0, at, 2):
			insertDots(newStr, i)

	def allDots(str):
		for i in range(0, len(str), 2):
			insertDots(str,i)


	allDots(email.replace(".", ""))

	print len(emailList)

	i = 1
	num = 0

	for mail in emailList[1901:2100]: #1439105125402
		requestURL = "https://invites.oneplus.net/index.php?r=share/signup&success_jsonpCallback=success_jsonpCallback&email={0}@gmail.com&koid={1}&_=1439220760537".format(mail, koid)
		print "Sending invite to  " + mail
		res = requests.get(requestURL)
		if(res.status_code == 200):
			print "Successfully retrieved response"
		else:
			print "Oneplus servers are babies, request failed"
			failed.append(mail)
		print str(i) + "/" + str(len(emailList))
		i = i + 1
		time.sleep(3)

print failed

with open('failed.txt', 'w') as outfile:
	json.dump(failed, outfile)
