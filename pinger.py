import subprocess
import os
import pyfiglet
from colorama import Fore

ascii_banner = pyfiglet.figlet_format("IPv4 SCANNER")
print(ascii_banner)
hint="""
by xd2mar | Twitter:@QK9
    """ 
print(hint)
ip1=input("#> Enter IP Here: > ")
x1=(ip1[:-1])
x2=(ip1[:-2])
x3=(ip1[:-3])

if len(ip1) < 7 or len(ip1) > 16:

        print("\n\tPlease enter a correct IP ")

elif x1[-1] == "." :
        with open(os.devnull, "wb") as limbo:
                print("checking now ip : {}(1-255)".format(x1))
                for n in range(1, 255):
                        ip = x1 + "{0}".format(n)
                        result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                                  stdout=limbo, stderr=limbo).wait()
                        if result:
                                print(Fore.LIGHTRED_EX +ip, "inactive")
                        else:
                                print(Fore.LIGHTGREEN_EX +ip,"active")
elif x2[-1] == "." :
        with open(os.devnull, "wb") as limbo:
                print("checking now ip : {}(1-255)".format(x2))
                for n in range(1, 255):
                        ip = x2 + "{0}".format(n)
                        result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                                  stdout=limbo, stderr=limbo).wait()
                        if result:
                                print(Fore.LIGHTRED_EX + ip, "inactive")
                        else:
                                print(Fore.LIGHTGREEN_EX + ip, "active")

elif x3[-1] == "." :
        with open(os.devnull, "wb") as limbo:
                print("checking now ip : {}(1-255)".format(x3))
                for n in range(1, 255):
                        ip = x3 + "{0}".format(n)
                        result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                                  stdout=limbo, stderr=limbo).wait()
                        if result:
                                print(Fore.LIGHTRED_EX + ip, "inactive")
                        else:
                                print(Fore.LIGHTGREEN_EX + ip, "active")

else:

        print("\n\tPlease enter a correct IP ")


