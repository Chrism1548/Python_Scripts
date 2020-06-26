# This Script will backup the running config of a Switch or Router
import getpass
import telnetlib
import datetime
import time


user = input('Enter Your Password')
password = getpass.getpass()
DT = datetime.datetime.now().strftime('%b-%w-%Y-%I-%M-%S-%p') #('Date-%b-%w-%Y--Time-%I-%M-%S-%p')    #replace(microsecond=0)
D = open('devices.txt')

for IP in range (211,219):                               # This code is using Ranges to configure the IP address
    HOST = '172.16.20.' + str(IP)                        # for the code to connect to
    tn = telnetlib.Telnet(HOST)
    print('Logging into host 172.16.20.' + str(IP))

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b'\n')


    #This section uses the TFTP server to backup the switch/router config
    print('Backing up config')
    tn.write(b'copy running-config tftp:\n')             # This can be changed to startup-config
    tn.write(b'172.16.20.2\n')                           # This can be changed to your TFTP server address
    tn.write(b'Backup_of_config-' + b'172.16.20.' + str(IP).encode('ascii') + b'-' + str(DT).encode('ascii') + b'.txt' +b'\n')
    tn.write(b'exit\n')
    time.sleep(1)                                        # This will time delay of the execution of the script

    print('Backup has been transferred to TFTP server folder')

    tn.close()

