#!/bin/bash

# arguments 
# $1 : interface DHCP
if [ -z "$1" ]; then
    echo "Usage: $0 <interface>"
    exit 1
fi

config_dhcp="
auto $1
iface $1 inet dhcp
"

echo "$config_dhcp" >> /etc/network/interfaces
systemctl restart networking