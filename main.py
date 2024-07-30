import ipaddress
from colorama import Fore, Style, init

# Initialize colorama
init()

def subnet_calculator(ip, subnet_mask, num_subnets):
    try:
        # Create an IP network object
        network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
        
        # Calculate the number of new bits needed to create the required number of subnets
        original_prefix_length = network.prefixlen
        subnet_bits = 0
        
        while (2 ** subnet_bits) < num_subnets:
            subnet_bits += 1
        
        new_prefix_length = original_prefix_length + subnet_bits
        if new_prefix_length > 32:
            raise ValueError("The number of requested subnets exceeds the maximum possible with this network.")
        
        # Calculate new subnets
        new_networks = list(network.subnets(new_prefix=new_prefix_length))
        
        # Print subnet details with colors
        print(Fore.CYAN + Style.BRIGHT + f"Original Network: {network}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Original Subnet Mask: {ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask}').netmask}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Number of Subnets Requested: {num_subnets}" + Style.RESET_ALL)
        print(Fore.BLUE + f"New Prefix Length: /{new_prefix_length}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"New Subnet Mask: {ipaddress.IPv4Network(f'0.0.0.0/{new_prefix_length}').netmask}" + Style.RESET_ALL)
        
        for idx, subnetwork in enumerate(new_networks):
            print(Fore.RED + Style.BRIGHT + f"\nSubnet {idx + 1}:" + Style.RESET_ALL)
            print(Fore.GREEN + f"  Network Address: {subnetwork.network_address}" + Style.RESET_ALL)
            print(Fore.GREEN + f"  Broadcast Address: {subnetwork.broadcast_address}" + Style.RESET_ALL)
            usable_ips = list(subnetwork.hosts())
            if usable_ips:
                print(Fore.GREEN + f"  Usable IP Range: {usable_ips[0]} - {usable_ips[-1]}" + Style.RESET_ALL)
                print(Fore.GREEN + f"  Total Usable IPs: {len(usable_ips)}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "  No usable IPs in this subnet." + Style.RESET_ALL)
    
    except ValueError as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

# Example usage
if __name__ == "__main__":
    ip = input(Fore.YELLOW + "Enter IP address (e.g., 10.10.10.0): " + Style.RESET_ALL)
    subnet_mask = input(Fore.YELLOW + "Enter subnet mask (e.g., 24 for 255.255.255.0): " + Style.RESET_ALL)
    num_subnets = int(input(Fore.YELLOW + "Enter number of subnets required: " + Style.RESET_ALL))
    
    subnet_calculator(ip, subnet_mask, num_subnets)
