import subprocess
from .colors import bcolors

def MyDetails():
    raw_res = subprocess.check_output('/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I', shell=True, encoding='utf-8')
    print('\n', f"{bcolors.OKBLUE}Details of your connetion:{bcolors.ENDC}\n", raw_res)
    exit()