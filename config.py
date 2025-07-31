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
        cfg_input = input("Enter configurations to write (comma-separated): ")
        config = [cfg.strip() for cfg in cfg_input.split(',')]
        
        for cfg in config:
            output = session.send_config_set(config)
            print(f"\n📄 Output from '{ip}':\n{output}")
            break
            
        session.disconnect()

    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")