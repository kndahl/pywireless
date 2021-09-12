import subprocess
from .colors import bcolors

def PublicIP():
    ip_raw = subprocess.check_output('dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com', shell=True, encoding='utf-8')
    print('\n', f"{bcolors.OKBLUE}Public IP address:{bcolors.ENDC}\n", ip_raw.replace('"', ""))
    exit()