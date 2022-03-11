
import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    print(dump)
    dump = dump.splitlines()
    
    for ip in dump:
    
        os.system('ping -n 2 {}' .format(ip))
        time.sleep(3)
        print('=+'*30)
    