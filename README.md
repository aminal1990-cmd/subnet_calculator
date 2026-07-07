# Subnet Calculator

A Python command-line tool for calculating IPv4 subnets using VLSM (Variable Length Subnet Masking).

## Features

- Splits a base network into a custom number of subnets
- Calculates the new subnet mask (CIDR prefix and dotted decimal, e.g. `255.255.255.192`)
- Computes Network Address, Broadcast Address, and usable host range for each subnet
- Validates user input (IP format, prefix range, subnet count)

## How to run

```bash
python3 subnet_calculator.py
```

You'll be prompted for:
- Base network IP (e.g. `192.168.10.0`)
- Original prefix (e.g. `24`)
- Number of subnets needed (e.g. `4`)

## Example output

```
Enter the base network IP: 192.168.10.0
Enter the original prefix (e.g. 24): 24
Enter the subnet's number: 4

new prefix: 26
subnet mask: 255.255.255.192
addresses per subnet: 64
usable hosts: 62

subnet 1: 192.168.10.0/26 | (broadcast: 192.168.10.63) | (Usable: 192.168.10.1 - 192.168.10.62)
subnet 2: 192.168.10.64/26 | (broadcast: 192.168.10.127) | (Usable: 192.168.10.65 - 192.168.10.126)
subnet 3: 192.168.10.128/26 | (broadcast: 192.168.10.191) | (Usable: 192.168.10.129 - 192.168.10.190)
subnet 4: 192.168.10.192/26 | (broadcast: 192.168.10.255) | (Usable: 192.168.10.193 - 192.168.10.254)
```
## What I learned building this

This project was built step-by-step while studying for CompTIA Network+, to connect subnetting theory (CIDR, host bits, network/broadcast addresses) with practical Python (loops, string manipulation, input validation, f-strings).
