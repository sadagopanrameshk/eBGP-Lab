from netmiko import ConnectHandler

# Get a comma-separated list of IPs from the user
ip_list = input("Enter device IPs separated by comma: ")

# Strip any extra spaces
ip_list = [ip.strip() for ip in ip_list.split(',')]

# Loop through each IP address and connect
for ip in ip_list:
    device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco'
    }

    try:
        print(f"\nConnecting to device {ip}...")
        session = ConnectHandler(**device)
        session.enable()
        
        print(f"you are in terminal of {ip}:")
        cmd_input = input("Enter CLI commands (comma-separated): ")
        commands = [cmd.strip() for cmd in cmd_input.split(',')]
        
        for cmd in commands:
            output = session.send_command(cmd)
            print (f"output of {cmd}: is \n {output}\n")
            break
            
        session.disconnect()

    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")


# import os
# from netmiko import ConnectHandler

# device={'device_type':'cisco_ios', 'ip':'192.168.1.12', 'username':'admin', 'password':'cisco', 'secret':'cisco'}

# session=ConnectHandler(**device)
# session.enable()

# # sh_cmd = ['sh ip int bri', ' sh ip bgp smm']

# # for cmd in sh_cmd:
    # # output=session.send_command(cmd)
    # # print(f"\n output from {device['ip']} '{cmd}' is:\n {output}")

# # 📝 Ask for commands to run
# cmd_input = input("Enter CLI commands (comma-separated): ")
# commands = [cmd.strip() for cmd in cmd_input.split(',')]

# # 🚀 Execute commands
# for cmd in commands:
    # output = session.send_command(cmd)
    # print (f"output of {cmd}: is \n {output}\n")

# session.disconnect()

