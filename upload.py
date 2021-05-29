import requests
import argparse



url = 'http://192.168.65.132:8080/api/v2/import-scan/'
headers = {'Accept': 'application/json',
           'Authorization': 'Token 97a73cd02f5643f9ff1847c6deb790f7382b0048'}






files = {'file': open('bandit-output.json','rb')}


formdata = {
    'scan_date': date,
    'minimum_severity': 'Info',
    'active': 'true',
    'verified':'true',
    'scan_type':'Bandit Scan',
    'engagement':'1',
    'lead':'1',
    'push_to_jira':'false',
    'close_old_findings':'false'
}


print(headers)
print(formdata)

r = requests.post(url, headers=headers, data=formdata, files=files) 

for item in r:
   print(item)