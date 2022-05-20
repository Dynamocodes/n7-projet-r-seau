#!/usr/bin/env python3

# ATTENTION!
# Pas de VPN
# Pas la config OSPF Zebra

import os
import sys
import subprocess

# -------------------------------------------------------------

# Configure interfaces
def config_interfaces(interface_definitions):
  for interface in interface_definitions:
    print("[*] Bringing up interface {} with address {}".format(interface['name'], interface['ip']))
    os.system("ip link set dev {} up".format(interface['name']))
    os.system("ip addr add {} dev {}".format(interface['ip'], interface['name']))

def config_routes(route_definitions):
  for route in route_definitions:
    print("[*] Adding route to {} via {} ({})".format(route['dest'], route['via'], route['interface']))
    os.system("ip route add {} via {} dev {}".format(route['dest'], route['via'], route['interface']))

# Enable IP Forward
def enable_ipforward():
  with open("/proc/sys/net/ipv4/ip_forward", "w+") as ip_forward_config:
    ip_forward_config.write("1")
  print("[*] IP Forward enabled")

# Enable Quagga
def config_quagga():
  print("[*] Configuring Quagga")
  with open("/etc/quagga/daemons", "w+") as quagga_config:
    quagga_config.writelines([
      "zebra=yes\n",
      "bgpd=no\n",
      "ospfd=yes\n",
      "ospf6d=no\n",
      "ripd=no\n",
      "ripngd=no\n",
      "isisd=no\n",
      "babeld=no\n"
    ])
  print("[*] Restarting Quagga")
  os.system("systemctl restart quagga")

# Configure DHCP Server
def config_dhcp_server(interface_name):
  print("[*] Installing DHCP")
  os.system("apt-get -y update && apt-get -y install isc-dhcp-server")
  with open("/etc/default/isc-dhcp-server", "w+") as isc_config:
    isc_config.writelines(["\n", "INTERFACES={}\n".format(interface_name)])
  print("[*] Configured ISC DHCP")
  with open("/etc/dhcp/dhcp.conf", "w+") as dhcp_config:
    dhcp_config.writelines([
      "default-lease-time 86400;\n",
      "max-lease-time 172800\n;",
      "option subnet-mask 255.255.255.0;\n",
      "option broadcast-address 120.0.7.255;\n",
      "subnet 120.0.7.0 netmask 255.255.255.0 {\n",
      "\trange 120.0.7.2 120.0.7.254;\n",
      "\toption domain-name-servers 120.0.5.2;\n",
      "\toption routers 120.0.7.1;\n", 
      "}\n"
    ])
  print("[*] Configured DHCP daemon")
  os.system("systemctl start isc-dhcp-server && systemctl enable isc-dhcp-server")
  print("[*] Started DHCP daemon")

# Configure DNS
def config_dns_server():
  print("[*] Configuring DNS Server")
  with open("/etc/bind/named.conf.default-zones", "a+") as dns_config:
    dns_config.writelines([
      "zone \"flamin.go\" {\n",
      "\ttype master;\n",
      "\tfile \"/etc/bind/flamin.go.db\";\n",
      "};\n"
    ])
  print("[*] Configuring domains")
  with open("/etc/bind/flamin.go.db", "w+") as flamingo_config:
    flamingo_config.writelines([
      "$TTL	604800\n",
      "@	IN	SOA	flamin.go. root.flamin.go. (\n",
      "			      2		; Serial\n",
      "			 604800		; Refresh\n",
      "			  86400		; Retry\n",
      "			2419200		; Expire\n",
      "			 604800\n",
      "); Negative Cache TTL\n",
      "@	IN	NS	flamin.go.\n",
      "@	IN	A	120.0.5.1\n",
      "@	IN	TXT	\"RICARD\"\n",
      "adri    IN      A       120.0.5.2\n",
      "voyd	IN	A	120.0.5.1\n",
    ])
  print("[*] Applying DNS configuration")
  os.system("named-checkconf && service bind9 restart")
  print("[*] Changing DNS resolver")
  with open("/etc/resolv.conf", "a") as resolv:
    resolv.write("nameserver 127.0.0.1\n")

# Configure DHCP Client
def config_dhcp_client(interface_name):
  print("[*] Configuring DHCP Client")
  with open("/etc/network/interfaces", "w+") as file:
    file.writelines([
      "auto {}\n".format(interface_name),
      "iface {} inet dhcp\n".format(interface_name),
    ])
  print("[*] Restarting networking")
  os.system("systemctl restart networking")

# Config VPN
def config_vpn():
  print("[*] Installing Wireguard")
  subprocess.run("apt-get -y update", stdout=subprocess.DEVNULL, shell=True)
  subprocess.run("apt-get -y install wireguard", stdout=subprocess.DEVNULL, shell=True)
  
  with open("/etc/wireguard/private.key", "w+") as private_key:
    subprocess.run("wg genkey", stdout=private_key, shell=True)
    subprocess.run("chmod go= /etc/wireguard/private.key", stdout=subprocess.DEVNULL, shell=True)
  
  private = subprocess.Popen("cat /etc/wireguard/private.key", stdout=subprocess.PIPE, shell=True)
  with open("/etc/wireguard/public.key", "w+") as public_key:
    subprocess.run("wg pubkey", stdin=private.stdout, stdout=public_key, shell=True)

  with open("/etc/wireguard/wg0.conf", "w+") as wg0:
    wg0.writelines([
      "[Interface]\n",
      "PrivateKey = {}\n".format(open("/etc/wireguard/private.key").read()),
      "Address = 10.8.0.1/24\n",
      "ListenPort = 51820\n",
      "SaveConfig = true\n"
    ])

# Download and start TeamSpeak server
def service_teamspeak():
  download_url = "https://files.teamspeak-services.com/releases/server/3.13.6/teamspeak3-server_linux_amd64-3.13.6.tar.bz2"
  download_path = "~/Téléchargements/"

  print("[*] Downloading TeamSpeak server")
  os.system("wget {} -P {}".format(download_url, download_path))
  print("[*] Extracting TeamSpeak server archive")
  os.system("tar -xf {} -C {}".format(download_path + "teamspeak3-server_linux_amd64-3.13.6.tar.bz2", download_path))
  print("[*] Starting TeamSpeak server")
  os.system(
    "{} {}/teamspeak3-server_linux_amd64/ts3server_startscript.sh start serveradmin_password=password virtualserver_codec_encryption_mode=1"
    .format("TS3SERVER_LICENSE=accept", download_path)
  )

def bold(text):
  return "\033[1m" + text + "\033[0m"

def red(text):
  return "\033[31m" + text + "\033[0m"

def print_help():
  print("Usage: sudo {} <role> [<args>]\n".format(sys.argv[0]))
  print("{} Exécute le script avec les droits {} batard!".format(bold(red("ATTENTION!")), bold("root")))
  print("Liste des roles:")
  print("  RU* (Routeur Utilisateur)\t\t*Argument additionnel pour l'interface qui fait du DHCP")
  print("  RA (Routeur d'Accès Entreprise)")
  print("  RI (Routeur d'Interconnexion)")
  print("  RE (Routeur Interne d'Entreprise)")
  print("  SE (Serveur d'Entreprise)")
  print("  CL (Client relié au RU)")

# -------------------------------------------------------------

role = sys.argv[1]

if sys.argv[1] in ["-h", "--help", "help"]:
  print_help()
  sys.exit(0)

# Configure RU (Routeur Utilisateurs)
if role in ["ru", "RU", "routeur-utilisateur"]:
  if len(sys.argv) < 3:
    print("Donne une interface batard (sudo <script> RU <interface>)")
    sys.exit(1)
  enable_ipforward()
  config_interfaces([
    {"name": "eth1", "ip": "120.0.3.1/24"},
    {"name": "eth2", "ip": "120.0.2.2/24"},
    {"name": "eth3", "ip": "120.0.7.1/24"}
  ])
  config_quagga()
  config_dhcp_server(sys.argv[2])
  sys.exit(0)

# Configure RA (Routeur d'Accès Entreprise)
elif role in ["ra", "RA", "routeur-acces"]:
  enable_ipforward()
  config_interfaces([
    {"name": "eth1", "ip": "120.0.1.1/24"},
    {"name": "eth2", "ip": "120.0.3.2/24"},
    {"name": "eth3", "ip": "120.0.5.1/24"}
  ])
  config_quagga()
  config_dns_server()
  sys.exit(0)

# Configure RI (Routeur d'Interconnexion)
elif role in ["ri", "RI", "routeur-interco"]:
  enable_ipforward()
  config_interfaces([
    {"name": "eth0", "ip": "10.192.0.4/29"},
    {"name": "eth1", "ip": "120.0.2.1/24"},
    {"name": "eth2", "ip": "120.0.1.2/24"}
  ])
  config_routes([
    {"dest": "120.0.16.0/24", "via": "10.192.0.1", "interface": "eth0"},
    {"dest": "120.0.32.0/24", "via": "10.192.0.2", "interface": "eth0"},
    {"dest": "120.0.48.0/24", "via": "10.192.0.3", "interface": "eth0"}
  ])
  config_quagga()
  sys.exit(0)

# Configure RE (Routeur Entreprise)
elif role in ["re", "RE", "routeur-ent"]:
  enable_ipforward()
  config_interfaces([
    {"name": "eth1", "ip": "120.0.5.2/24"},
    {"name": "eth2", "ip": "192.168.0.1/24"}
  ])
  config_routes([
    {"dest": "0.0.0.0/0", "via": "120.0.5.2", "interface": "eth1"},
    {"dest": "192.168.0.0/24", "via": "192.168.0.1", "interface": "eth2"}
  ])
  os.system("iptables -t nat -A POSTROUTING -o eth1 -j SNAT --to 120.0.5.2")
  os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -i eth1 -j DNAT --to 192.168.0.2:80")
  sys.exit(0)

# Configure SE (Serveur Entreprise)
elif role in ["se", "SE", "serveur-ent"]:
  config_interfaces([
    {"name": "eth2", "ip": "192.168.0.2/24"}
  ])
  config_routes([
    {"dest": "default", "via": "192.168.0.1", "interface": "eth2"}
  ])
  service_teamspeak()
  sys.exit(0)

# Configure CL (Client)
elif role in ["cl", "CL", "client"]:
  print("RAF")
  sys.exit(0)

# Configure REX (Routeur d'Entreprise Extérieur)
elif role in ["rex", "REX", "routeur-ext"]:
  config_interfaces([
    {"name": "eth0", "ip": "120.0.24.18/30"},
    {"name": "eth1", "ip": "120.0.8.1/24"}
  ])
  sys.exit(0)

# Configure CEX (Client d'Entreprise Extérieur)
elif role ["cex", "CEX", "client-ext"]:
  config_interfaces([
    {"name": "eth0", "ip": "120.0.8.2/24"}
  ])
  sys.exit(0)