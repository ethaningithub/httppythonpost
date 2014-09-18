#!/usr/bin/python

from requests_toolbelt import MultipartEncoder
import requests
import json
import time

json_data = open('key')
data = json.load(json_data)


url = "http://event.snowmilk.com.tw/201409/vote_after_update.php"
length = len(data['phone_num'])
print length

for i in range(0,length-1):
	payload = {
		'act': 'new',
		'serialno': '2799',
		'mobile': data['phone_num'][i],
		'votepwd': data['password'][i],
	}
#payload = MultipartEncoder({'act':'new','serialno':'2799','mobile':'0933216533','votepwd':'K5PFx9Dj'})
#payload1 = {'votepwd': 'K5PFx9Dj'}
	r = requests.post(url, data=payload)
	print "iteration times: ",i,"\n"
	print(r.text)
	time.sleep(3)
#with open("requests_result.html", "w") as f:
#	f.write(r.content)
