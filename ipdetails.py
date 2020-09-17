import requests
from requests.exceptions import HTTPError
import time

try:
	ip1 = open("ip.txt","r")
	ipread = ip1.readlines()
	i = 1
	for ip in ipread:
		#print ip 
		ip = ip.rstrip()
		ip = ip.lstrip()
 		url = 'http://ip-api.com/json/'+ip
		#print url
    		response = requests.get(url)
		response.raise_for_status()
		jsonResponse = response.json()
    		for key, value in jsonResponse.items():
			print i,',',ip,',',key,',',value
			#if key == "org":
				#print ip,':',value
        			#print key,':', value
 		i=i+1
		if i==45:
			#print "I am sleeping for 60sec"
			time.sleep(60)
		else:
			#print "I am sleeping for 5sec"
			time.sleep(2)
except HTTPError as http_err:
    print('HTTP error occurred: {http_err}')
except Exception as err:
    print('Other error occurred: {err}')
