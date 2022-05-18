#!/bin/bash

# arguments 
# $1 : interface DHCP

config_dhcp="
auto $1
\n iface $1 inet dhcp
"

echo $config_dhcp >> /etc/network/interfaces
systemctl restart networking