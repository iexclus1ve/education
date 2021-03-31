# /usr/bin/env python

import paramiko
import getpass

client = paramiko.SSHClient()

control = 'systemctl'
actionStart = 'start'
actionStop = 'stop'
promt = 'sudo'

host = input('Enter IP address or hostname: ')
port = int(input('Enter port number: '))
username = input('Enter username: ')
password = getpass.getpass('Enter password: ')
serviceName = input('Enter a service e. g. "nginx": ')

serviceStart = f'{promt} {control} {actionStart} {serviceName}'
serviceStop = f'{promt} {control} {actionStop} {serviceName}'

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host,
               port,
               username,
               password)

client.get_transport()

print('Connection Success!')

while True:

    commandAction = input('Enter 1 for START service or 0 for STOP service: ')

    try:
        commandAction = int(commandAction)
    except ValueError:
        print('Enter a correct value')
    if commandAction == 1:
        command = serviceStart
        print(f'Service {serviceName.upper()} will be starting')
        break
    elif commandAction == 0:
        command = serviceStop
        print(f'Service {serviceName.upper()} will be stopping')
        break
    else:
        print('WTF?! Please enter 0 or 1')

try:
    stdin, stdout, stderr = client.exec_command(command=command, get_pty=True)
    print('Command sent')
    stdin.write(password + '\n')
    print('Password sent')
    stdin.flush()
    print('Input flushed')

    if stderr.channel.recv_exit_status() != 0:
        print('Error occured!')
        print(f'The following error occured: {stderr.readlines()}')
    else:
        print('Getting output!')
    #   print(f"The following output was produced: \n{stdout.readlines()}")

    client.close()
    print('Have a nice day.')
except Exception:
    print('Unknown command')