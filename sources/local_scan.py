
import requests,sys
from .colors import bcolors

import paramiko

def LocalScan():

    # # IP of Cloudlabs AOS Server
    # server = '192.168.1.1'
    # username = 'admin'
    # password = 'admin'

    # # authenticate and get a auth token
    # url = 'http://' + server + '/login'
    # headers = { 'Content-Type':"application/json", 'Cache-Control':"no-cache" }
    # data = '{ \"Username\":\"' + username + '\", \"Password\":\"' + password + '\" }'
    # response = requests.post(url, data=data, headers=headers, verify=False, timeout=(30,200))
    # print(response)
    # print('POST',url,response.status_code)
    # if response.status_code != 201:
    #     print(data)
    #     sys.exit(f'{bcolors.FAIL}Error: authentication failed{bcolors.ENDC}')
    # auth_token = response.json()['token']
    # print(auth_token)
    # headers = { 'AuthToken':auth_token, 'Content-Type':"application/json", 'Cache-Control':"no-cache" }


    ssh = paramiko.SSHClient()
    ssh.connect( 'hostname', username = 'admin', password = 'admin' )
    ssh.exec_command( 'ls -al' )