# /usr/bin/env python

import paramiko
import getpass

client = paramiko.SSHClient()

control = 'systemctl'
serviceName = 'openvpn@server'
actionStart = 'start'
actionStop = 'stop'
promt = 'sudo'


commandStart = f'{promt} {control} {actionStart} {serviceName}'
commandStop = f'{promt} {control} {actionStop} {serviceName}'

host = input('Enter IP address or hostname: ')
port = int(input('Enter port number (default 22): '))

username = input('Enter username: ')
password = getpass.getpass('Enter password: ')

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username, password)
client.get_transport()
print('Connection Success!')


command = int(input('Enter 1 for START service or 0 for STOP service: '))

for i in range(3):
    if command == 1:
        command = commandStart
        print('Service will be start')
    elif command == 0:
        command = commandStop
        print('Service will be stop')
    else:
        print('Enter a correct value')


stdin, stdout, stderr = client.exec_command(command=command, get_pty=True)
print("command sent!")
stdin.write(password + '\n')
print("Password sent!")
stdin.flush()
print("Input flushed!")

if stderr.channel.recv_exit_status() != 0:
    print("Error occured!")
    print(f"The following error occured: {stderr.readlines()}")
else:
    print("Getting output!")
    print(f"The following output was produced: \n{stdout.readlines()}")

client.close()
