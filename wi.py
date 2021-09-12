from tabulate import tabulate
import pandas as pd
from global_scan import GlobalScan
from local_scan import LocalScan
import subprocess
import socket

#df = pd.DataFrame(columns = ["SSID"])

def MyDetails():
    raw_res = subprocess.check_output('/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I', shell=True, encoding='utf-8')
    print('\n', "Details of your connetion:\n\n", raw_res)
    exit()

def SocketName():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("\nFounded local IP adresses:\n",s.getsockname()[0])
    s.close()
    exit()

_table = [["Find all users connected to your wifi network" , 1], ["Global scan", 2], ['Details of my connection', 3], ['Local IP addresses', 4], ["Quit", "q"]]
table = tabulate(_table, headers=['What do you want to scan?','Press'], tablefmt='orgtbl')

while True:
    print(table)
    answer = input("> ")
    if answer is 'q':
        exit()
    if answer is '1':
        LocalScan()
    if answer is '2':
        GlobalScan()
    if answer is '3':
        MyDetails()
    if answer is '4':
        SocketName()