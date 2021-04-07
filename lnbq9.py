#import psutil
import os, platform,uuid

def menu():
    print('Enter 1 get the MAC address\n'
        'Enter 2 get the RAM and CPU details.\n'
        'Enter 3 get the OS information\n'
        'Enter 4 to exit : ')
    
menu()
choice=int(input('Enter your option:'))

while choice != 4:          
    if choice == 1:
        print (hex(uuid.getnode()))

    elif choice == 2:
        print('The CPU usage is: ', psutil.cpu_percent(4))
   
    elif choice == 3:
        print(os.name)
        print(platform.system())
        print(platform.release())
        
    menu()
    choice=int(input('Enter your option:'))