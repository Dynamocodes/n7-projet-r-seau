#!/bin/bash

# arguments 
# $1 : interface DHCP
if [ -z "$1" ]; then
    echo "Usage: $0 <interface>"
    exit 1
fi

# Config DHCP pour le client
apt update
apt install isc-dhcp-server

# isc-dhcp-server config
config="
INTERFACES=\"$1\"
"

# write config in isc-dhcp-server file
echo "$config" > /etc/default/isc-dhcp-server

config_dhcp="
# Configuration DHCP
default-lease-time 600;
max-lease-time 7200;
option subnet-mask 255.255.255.0;
option broadcast-address 120.0.7.255;
option domain-name-servers 8.8.8.8;
option domain-name \"reseau.acces.as0\";
option routers 120.0.7.1;

subnet 120.0.7.0 netmask 255.255.255.0 {
	range 120.0.7.2 120.0.7.254;
}
"

# write config in dhcpd config file
echo "$config_dhcp" > /etc/dhcp/dhcp.conf

# start dhcp
systemctl start isc-dhcp-server
systemctl enable isc-dhcp-server
systemctl enable isc-dhcp-server

# permit requests to DHCP daemon on Firewall
# ufw allow 67/udp
# ufw reloa