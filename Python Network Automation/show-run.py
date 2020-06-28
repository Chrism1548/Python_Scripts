import getpass
import telnetlib

HOST = '172.16.20.211'
user = 'chris'
password = 'cisco'

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b'conf t\n')
tn.write(b'int l1\n')
tn.write(b'ip add 1.1.1.1 255.255.255.255\n')
tn.write(b'exit\n')
tn.write(b'exit\n')
tn.write(b"terminal length 0\n")
tn.write(b"sh run\n")
tn.write(b'exit\n')

print(tn.read_all().decode('ascii'))

tn.close() 