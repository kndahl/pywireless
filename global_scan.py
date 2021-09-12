import subprocess

def GlobalScan():
    print("Scaning...")
    raw_res = subprocess.check_output('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport --scan', shell=True, encoding='utf-8')
    print("\nScaned all wireless networks\n\n", raw_res)
    exit()