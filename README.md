# Subnet-Calculator
  A Python script to calculate subnets for a given IPv4 network, subnet mask, and the number of required subnets. This tool uses the ip address module for handling IPv4 networks and colorama for colorful output.
## Features
  Calculates the new subnets based on the original network and required number of subnets.
Displays the network address, broadcast address, usable IP range, and total usable IPs for each new subnet.
Provides color-coded output for better readability.

### Requirements
  (1) Python 3.x
  
  (2) Ip Address module (included in Python standard library)
  
  (3) Colorama module

### Installation
###  1. Clone the repository
    git clone https://github.com/byt3b4nd/Subnet-Calculator.git

### 2. Navigate to the project directory:
      cd subnet-calculator
### 3. Install the required package:
      pip install colorama


### Usage
### Run the script and follow the prompts to enter the IP address, subnet mask, and the number of subnets required:
    python main.py

### Example input:
      Enter IP address (e.g., 10.10.10.0): 192.168.1.0
      Enter subnet mask (e.g., 24 for 255.255.255.0): 24
      Enter number of subnets required: 4

### Example output:
      Original Network: 192.168.1.0/24
      Original Subnet Mask: 255.255.255.0
      Number of Subnets Requested: 4
      New Prefix Length: /26
      New Subnet Mask: 255.255.255.192

      Subnet 1:
      Network Address: 192.168.1.0
      Broadcast Address: 192.168.1.63
      Usable IP Range: 192.168.1.1 - 192.168.1.62
      Total Usable IPs: 62

      Subnet 2:
      Network Address: 192.168.1.64
      Broadcast Address: 192.168.1.127
      Usable IP Range: 192.168.1.65 - 192.168.1.126
      Total Usable IPs: 62



        

        



    
       
