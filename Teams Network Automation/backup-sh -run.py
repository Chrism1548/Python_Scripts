# This Script will backup the running config of a Switch or Router
import getpass
import telnetlib
import datetime
import time

# This section will prompt for username and password
user = input('Enter Your Password')
password = getpass.getpass()
DT = datetime.datetime.now().strftime('%b-%d-%Y-%I-%M-%S-%p') #('Date-%b-%d-%Y--Time-%I-%M-%S-%p')    #replace(microsecond=0)
D = open('devices.txt')

for AD in D:
    AD = AD.strip()                                        # Removes white spaces from start and end of line in file
    HOST = AD

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b'\n')
        print('Logging into ' + AD)


    # This Section will copy the start/running config of the switch/router
    print('Backing up config')
    tn.write(b'terminal length 0\n')
    tn.write(b'sh run\n')                                  # sh run can be replaced with sh start
    tn.write(b'exit\n')
    time.sleep(1)                                          # This will time delay of the execution of the script

    # Save running config to folder
    print('Saving Backup to Folder')
    readoutput = tn.read_all().decode('ascii')
    filepath = b'C:\Users\Chris\Downloads\Backups\ '      # Change file path to your own
    PATH = filepath.decode('ascii')
    saveoutput = open(PATH + AD + '-' + str(DT) + '-' + '.txt', 'w')
    saveoutput.write(str(readoutput))
    saveoutput.close()
    #print(readoutput)
    print(len(readoutput))                                # This will print out the number of characters in the output

    tn.close()


