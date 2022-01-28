""
CBUser.py
Chadd Horanburg - 12 August, 2021

This script will read a CSV file with user details and then
create the necessary users in the CB Cloud Consoles (MSSP Consoles)

https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/user-management/
https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/access-profiles-and-grants/
"""

import requests
import json
import configparser
from requests import cookies
import csv
import urllib3
from urllib3.exceptions import SystemTimeWarning
#urllib3.disable_warnings()

# Import config file
config = configparser.ConfigParser()
config.read('config')
APIKey = config['APICore']['APIKEY']
APIID = config['APICore']['APIID']
CBInstance = config['APICore']['CBInstance']
OrgKey = config['APICore']['OrgKey']
OrgID = config['APICore']['OrgID']
role = config['Options']['Role']


headers = {
    'X-Auth-Token':f"{APIKey}"+"/"+f'{APIID}',
    'Content-Type': 'application/json',
}

def addUser(firstName,LastName,email):
    addUserData = '{"first_name":"' +str(firstName) + '","last_name":"' +str(LastName) + '","email":"' +str(email) + '","role":"DEPRECATED","role_urn":"psc:role:7VRAEKL7:TD-BASE"}'
    #try:
    response = requests.post('https://' +str(CBInstance)+ '/appservices/v6/orgs/' +str(OrgKey)+ '/users', headers=headers, data=addUserData)
    #response.raise_for_status()
    #except requests.exceptions.RequestException as e:
        #raise SystemExit(e)
    print(response.text)

with open('users.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        userEmail = row[0]
        userID = userEmail.split('@',1)[0]
        userFirst = userID.split('.',1)[0]
        userLast = userID.split('.',2)[1]
        print("First Name: {}, Last Name {}, Email: {}".format(userFirst,userLast,userEmail))
        addUser(userFirst,userLast,userEmail)
