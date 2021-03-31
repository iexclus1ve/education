# /usr/bin/env python

import paramiko

client = paramiko.SSHClient()


client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.39', 22, 'support', 'usergatepass')
client.get_transport()

command = "sudo systemctl start openvpn@server"
stdin, stdout, stderr = client.exec_command(command=command, get_pty=True)
#print("command sent!")
stdin.write("usergatepass\n")
#print("Password sent!")
stdin.flush()
#print("Input flushed!")

if stderr.channel.recv_exit_status() != 0:
    print("Error occured!")
    print(f"The following error occured: {stderr.readlines()}")
else:
    print("Getting output!")
    print(f"The following output was produced: \n{stdout.readlines()}")

client.close()
