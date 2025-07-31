import os
from datetime import datetime
from netmiko import ConnectHandler

# Create backup folder
BACKUP_DIR = "./backups"
os.makedirs(BACKUP_DIR, exist_ok=True)

device={'device_type':'cisco_ios', 'ip':'192.168.1.12', 'username':'admin', 'password':'cisco', 'secret':'cisco'}

session=ConnectHandler(**device)
session.enable()

print("running backup")
backup=session.send_command('sh run')
filename = f"{device['ip']}_backup.txt"
path = os.path.join(BACKUP_DIR, filename)
with open(path, "w") as f:
    f.write(backup)
    print(f"Configuration backup saved in: {path}")
    
session.disconnect()
 
 



