
import requests,sys

def LocalScan():

    # IP of Cloudlabs AOS Server
    aos_server = '192.168.1.1'
    username = 'admin'
    password = 'admin'

    # authenticate and get a auth token
    url = 'http://' + aos_server + '/login'
    headers = { 'Content-Type':"application/json", 'Cache-Control':"no-cache" }
    data = '{ \"Username\":\"' + username + '\", \"Password\":\"' + password + '\" }'
    response = requests.request("POST", url, data=data, headers=headers, verify=False, timeout=(30,200))
    print(response)
    print('POST',url,response.status_code)
    if response.status_code != 201:
        sys.exit('error: authentication failed')
    auth_token = response.json()['token']
    print(auth_token)
    headers = { 'AuthToken':auth_token, 'Content-Type':"application/json", 'Cache-Control':"no-cache" }