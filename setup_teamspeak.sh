#!/bin/bash

ip addr add 120.0.5.2/24 dev eth2

wget https://files.teamspeak-services.com/releases/server/3.13.6/teamspeak3-server_linux_amd64-3.13.6.tar.bz2 -P ~/Téléchargements/

cd ~/Téléchargements/

tar -xf ~/Téléchargements/teamspeak3-server_linux_amd64-3.13.6.tar.bz2

TS3SERVER_LICENSE=accept ./teamspeak3-server_linux_amd64/ts3server_startscript.sh start serveradmin_password=password virtualserver_codec_encryption_mode=1
