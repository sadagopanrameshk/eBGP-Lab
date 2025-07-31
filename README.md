# 🚀 Loopback-Sourced eBGP Lab with GNS3 and Python Automation(Netmiko)

## 🧪 Lab Summary
Create an python Automated script to send configuration to Network Devices to establish eBGP session using Loopback interfaces for peering stability. 
Validate setup with Python scripts using Netmiko.

## 🖥 Topology
- Router1 (AS65001): Loopback 1.1.1.1, G0/0 192.168.1.11
- Router2 (AS65002): Loopback 2.2.2.2, G0/0 192.168.1.12

## ⚙️ Setup Highlights
- OSPF for Loopback reachability
- eBGP multihop + update-source Loopback0
- Prefix advertisement with correct mask

## 💻 Python Automation Script
- Get a list of IPs from the user to connect
- Loop through each IP address and connect
- Get a list of configuration commands from the user to configure in each device from IP list.

## 💻 Python Validator script
- Ping test via Loopback
- BGP session validation

## 📸 Screenshots
<img width="541" height="539" alt="image" src="https://github.com/user-attachments/assets/5cbb8f9b-a1d6-4a00-918e-03f23a90f884" />
<img width="578" height="631" alt="image" src="https://github.com/user-attachments/assets/e8c3ae14-fc6b-4614-b85f-cb6e8dbfb6b8" />
<img width="682" height="178" alt="image" src="https://github.com/user-attachments/assets/a1e1501d-887c-4364-9d9f-0227bb6d216e" />

