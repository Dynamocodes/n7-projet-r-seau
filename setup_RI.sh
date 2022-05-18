#!/bin/bash

# Monter les bonnes interfaces et brancher sur le bon port
ip link set dev eth1 up # Branché à la prise INT1-XX
ip link set dev eth2 up # Branché à la prise INT2-XX 

# ATTRIBUTION DES ADDRESSE
ip address add 120.0.6.1/24 dev eth0
ip address add 120.0.1.2/24 dev eth1
ip address add 120.0.2.1/24 dev eth2

# AUTORISER LE ROUTAGE
sysctl -w net.ipv4.ip_forward=1
