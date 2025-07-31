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
        print(f"\nConnecting to device {ip}... \n")
        session = ConnectHandler(**device)
        session.enable()
        
        ping_output = session.send_command("ping 1.1.1.1 source 2.2.2.2") if "192.168.1.12" in {ip} \
        else session.send_command("ping 2.2.2.2 source 1.1.1.1")
        
        bgp_summary = session.send_command("show ip bgp summary")
        
        print("📡 Ping Result:")
        print(f"{ping_output}\n")
        print("📊 BGP Summary:")
        print(f"{bgp_summary}\n" )
            
        session.disconnect()

    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")