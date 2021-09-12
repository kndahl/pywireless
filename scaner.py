from tabulate import tabulate
import pandas as pd
from sources.global_scan import GlobalScan
from sources.local_scan import LocalScan
from sources.local_ip import SocketName
from sources.my_connection import MyDetails
from sources.public_ip import PublicIP
from sources.colors import bcolors
import pyfiglet

import warnings
warnings.filterwarnings("ignore")


_table = [["Find all users connected to your wifi network" , 1], ["Global scan", 2], ['Details of my connection', 3], ['Local IP address', 4], ['Public IP address', 5], ["Quit", "q"]]
table = tabulate(_table, headers=[f"{bcolors.HEADER}What do you want to scan?{bcolors.ENDC}",f'{bcolors.OKCYAN}Press{bcolors.ENDC}'], tablefmt='orgtbl')

ascii_banner = pyfiglet.figlet_format("pywireless")
print(ascii_banner + "v0.0.1\tby kndahl")

while True:
    print('\n'+ table)
    answer = input("> ")
    if answer == 'q':
        exit()
    if answer == '1':
        LocalScan()
    if answer == '2':
        GlobalScan()
    if answer == '3':
        MyDetails()
    if answer == '4':
        SocketName()
    if answer == '5':
        PublicIP()
    else:
        print(f"{bcolors.WARNING}Incorrect!{bcolors.ENDC}")