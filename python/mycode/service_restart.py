# /usr/bin/env python

import paramiko
import getpass

client = paramiko.SSHClient()

commandStart = 'sudo systemctl start openvpn@server'
commandStop = 'sudo systemctl stop openvpn@server'
host = input('Enter IP address: ')
port = 22
username = input('Enter username: ')
password = getpass.getpass('Enter password: ')

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username, password)
client.get_transport()
print('Connection Success!')

command = commandStart
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
