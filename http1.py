import warnings
warnings.filterwarnings("ignore")

import json 
import requests
import time

cur_date = time.strftime("%d-%b-%Y_%H_%M")
print(cur_date)

url = "https://localhost:4087/api/"

payload0 = {
  "Username": "John",
  "Password": "1"
}

headers0 = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url+"auth/token", headers=headers0, data=json.dumps(payload0), verify=False)

im_token = response.json()['AccessToken']
print(im_token)



# Finding GUID for Part with Part Number = "Autotest"
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': ''
}

headers['Authorization'] = "Bearer " + im_token

payload = {
  'PartName': '',
  'PartNumber': 'Autotest',
  'Revision': '',
  'PartGUIDs': '',
  'PageSize': 0,
  'Page': ''
}

response2 = requests.post(url+'parts/list', headers=headers, data=json.dumps(payload), verify=False)

listParts = response2.json()
guid_part =  listParts['Parts'][0]['GUID']   
print(listParts)


# Clone Part

clone_part = {
  "PartGUID": "",
  "NewPartNumber": "",
  "NewPartName": "",
  "NewRevision": "A",
  "CopyMaterials": False,
  "CopyResults": True,
  "CopyReports": False
}
clone_part['PartGUID'] = guid_part
clone_part['NewPartNumber'] = 'Auto_' + cur_date
clone_part['NewPartName'] = 'Auto_' + cur_date

response = requests.post(url+'parts/clone', headers=headers, data=json.dumps(clone_part), verify=False)

print(response.json())





