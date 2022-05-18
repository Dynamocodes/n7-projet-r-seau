#!/bin/bash
sudo su
cp config_quagga /etc/quagga/daemons
systemctl restart quagga

