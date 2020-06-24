# This Script will backup the running config of a Switch or Router
import getpass
import telnetlib
import datetime
import time


user = input('Enter Your Password')
password = getpass.getpass()
DT = datetime.datetime.now().strftime('%b-%w-%Y-%I-%M-%S') #('Date-%b-%w-%Y--Time-%I-%M-%S')    #replace(microsecond=0)
D = open('devices.txt')

for AD in D:
    AD = AD.strip()
    HOST = AD

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b'\n')
        print('Logging into ' + AD)

    #This section uses the TFTP server to backup the switch/router config
    print('Backing up config')
    tn.write(b'copy running-config tftp:\n')             # This can be changed to startup-config
    tn.write(b'172.16.20.2\n')
    tn.write(b'sw-config-' + str(AD).encode('ascii') + b'-' + str(DT).encode('ascii') + b'.txt' +b'\n')
    tn.write(b'exit\n')
    time.sleep(1)                                        # This will time delay of the execution of the script


    tn.close()

