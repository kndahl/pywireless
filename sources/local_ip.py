import socket
from .colors import bcolors

def SocketName():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(f"\n{bcolors.OKBLUE}Founded local IP adresses:{bcolors.ENDC}\n",s.getsockname()[0])
    s.close()
    exit()