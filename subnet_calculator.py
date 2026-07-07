import math

base_ip = input("Enter the base network IP: ")
ip_parts = base_ip.split(".")
print(ip_parts)

ip_is_valid = True
if len(ip_parts) != 4:
    ip_is_valid = False
    print("Invalid IP address. Must have 4 octets.")
    exit()

for part in ip_parts:
    if not part.isdigit():
        ip_is_valid = False
    elif int(part) < 0 or int(part) > 255:
        ip_is_valid = False

if not ip_is_valid:
    print("Invalid IP address. Each octet must be between 0 and 255.")
    exit()

ip_prefix_str = ".".join(ip_parts[0:3])

last_octet = int(ip_parts[-1])

original_prefix = int(input("Enter the original prefix (e.g. 24): "))
print(original_prefix)

if original_prefix <= 0 or original_prefix >= 32:
    print("Invalid prefix. Must be between 0 and 32.")
    exit()

num_subnets = int(input("ٍEnter the subnet's number:  "))
print(num_subnets)

if num_subnets < 2:
    print("Number of subnets must be least 2.")
    exit()

bits_needed = math.ceil(math.log2(num_subnets))
print(f"bits needed: {bits_needed}")

new_prefix = original_prefix + bits_needed
host_bits = 32 - new_prefix

if new_prefix > 30:
    print("Invalid prefix. Must be less than or equal to 30.")
    exit()

print(f"new prefix: {new_prefix}")
print(f"host bits: {host_bits}")

#محاسبه سابنت مسک
remaining_network_bits = new_prefix
subnet_mask_parts = []

for i in range(4):
    if remaining_network_bits >= 8:
        byte_value = 255
        remaining_network_bits -= 8
    elif remaining_network_bits > 0:
        host_bits_in_byte = 8 - remaining_network_bits
        byte_value = 256 - 2 ** host_bits_in_byte
        remaining_network_bits = 0
    else:
        byte_value = 0
    subnet_mask_parts.append(byte_value)

subnet_mask_str = ".".join(str(x) for x in subnet_mask_parts)
print(f"subnet mask: {subnet_mask_str}")

addresses_per_subnet = 2 ** host_bits
print(f"addresses per subnet: {addresses_per_subnet}")

usable_hosts = addresses_per_subnet - 2
print(f"usable hosts: {usable_hosts}")

for i in range(num_subnets):
    network_start = last_octet + i * addresses_per_subnet
    broadcast = network_start +addresses_per_subnet - 1
    first_usable = network_start +1
    last_usable = broadcast - 1
    print(f"subnet {i + 1}: {ip_prefix_str}.{network_start}/{new_prefix} | (broadcast: {ip_prefix_str}.{broadcast})| (Usable: {ip_prefix_str}.{firs_usable} - {ip_prefix_str}.{last_usable})")