#!/bin/bash

# Activer le Packet Forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Monter les bonnes interfaces et brancher sur le bon port
ip link set dev eth1 up # Branché à la prise INT1-XX
ip link set dev eth2 up # Branché à la prise INT2-XX


# Associer l'ip à la bonne interface
ip addr add 120.0.3.1/24 dev eth1
ip addr add 120.0.2.2/24 dev eth2
