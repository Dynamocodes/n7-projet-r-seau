#!/bin/bash

cp config_quagga /etc/quagga/daemons
systemctl restart quagga

