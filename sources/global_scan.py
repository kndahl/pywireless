import subprocess
from .colors import bcolors

def GlobalScan():
    print("Scaning...")
    raw_res = subprocess.check_output('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport --scan', shell=True, encoding='utf-8')
    print(f"\n{bcolors.OKBLUE}Scaned all wireless networks{bcolors.ENDC}\n\n", raw_res)
    exit()