import requests
from requests.exceptions import HTTPError

try:
	ip1 = open("ip.txt","r")
	ipread = ip1.readlines()
	for ip in ipread:
		#print ip 
       		#ip2 = '18.130.203.48'
		ip = ip.rstrip()
		ip = ip.lstrip()
 		url = 'http://ip-api.com/json/'+ip
		#print url
    		response = requests.get(url)
		response.raise_for_status()
		jsonResponse = response.json()
    		for key, value in jsonResponse.items():
			if key == "org":
				print ip,':',value
        			#print(key, ":", value)
    
except HTTPError as http_err:
    print('HTTP error occurred: {http_err}')
except Exception as err:
    print('Other error occurred: {err}')
