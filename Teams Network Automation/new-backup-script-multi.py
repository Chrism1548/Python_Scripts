import getpass
import telnetlib


user = input('Enter Your Password')
password = getpass.getpass()
D = open('devices')

for AD in D:
    AD = AD.strip()
    HOST = AD

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b'\n')
        print('Logging into ' + (AD))


    tn.write(b'terminal length 0\n')
    tn.write(b'sh run\n')
    tn.write(b'exit\n')

    #save running config to folder
    readoutput = tn.read_all().decode('ascii')
    filepath = b'C:\Users\Chris\Downloads\Backups\ '
    device_name = filepath.decode('ascii')
    saveoutput = open(device_name + AD + '.txt', 'w')
    saveoutput.write(str(readoutput))
    saveoutput.close()
    print(readoutput)

    tn.close()


