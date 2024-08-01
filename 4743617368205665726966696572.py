import random
import sys
import os
import requests
import json
import colorama
r = "\033[31m"
g = "\033[32m"
w = "\033[37m"
os.system('cls')
print("""
\033[36m=======================================================================================================================
\033[36m=                                           \033[37mGCash Number Checker                                                      \033[36m=
\033[36m=======================================================================================================================
\033[36m=                                                                                                                     \033[36m=
\033[36m=   \033[32m██████╗  ██████╗ █████╗ ███████╗██╗  ██╗               ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗     \033[36m=
\033[36m=  \033[32m██╔════╝ ██╔════╝██╔══██╗██╔════╝██║  ██║              ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗    \033[36m= 
\033[36m=  \033[32m██║  ███╗██║     ███████║███████╗███████║    █████╗    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝    \033[36m=
\033[36m=  \033[32m██║   ██║██║     ██╔══██║╚════██║██╔══██║    ╚════╝    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗    \033[36m=
\033[36m=  \033[32m╚██████╔╝╚██████╗██║  ██║███████║██║  ██║              ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║    \033[36m=
\033[36m=   \033[32m╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝               ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    \033[36m=
\033[36m=======================================================================================================================
\033[36m=      \033[37mThis tool is 100% accurate because it uses GCash APIs directly can check valid logins to GCash Accounts.       \033[36m=
\033[36m=======================================================================================================================                                                     
""")
session = True

def mainFunction():
    session = True
    randomNumber = input("\033[32mEnter Phone Number: ")
    response = requests.post('https://mgs-gw.paas.mynt.xyz/mgw.htm','operationType=alipayplus.mobilewallet.user.login.consult&requestData=[{"envInfo":{"tokenId":"76116844-0287-4ee8-9d2c-d7af66cc12de","osType":"WindowsNT","osVersion":"10.0","browserType":"Chrome","browserVersion":"93","terminalType":"WEB"},"loginIdType":"MOBILE_NO","loginId":"' + randomNumber + '","extParams":{"bizNo":"","sessionId":null,"bizTypeForMonitor":"ONLINE_LAZADA","merchantForMonitor":""}}]&version=2.0&workspaceId=PROD&appId=D54528A131559&tenantId=MYNTPH','?ctoken=')
    res = response.text
    data = res.find("true")
    if 0 < data:
        print("\n\033[37m[" + randomNumber + "] \033[36m---> \033[32m[ GCash Registered ]")
    else:
        print("\n\033[37m[" + randomNumber + "] \033[36m---> \033[31m[ Not Registered in GCash ]")

while session:
    mainFunction()
    x = input("Scan another? (Y/n): ")
    if x.lower() == "y":
        mainFunction()
    else:
        print("thank you for using.")
        exit()
