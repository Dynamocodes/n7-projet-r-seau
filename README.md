# n7-projet-reseau
N° du groupe : 0
## TLDR:
Déploiement d'un AS interconnecté à d'autres AS, en suivant l'architecture réseau suivante
[Maquette Figma](https://www.figma.com/file/b7xy9bIjHuaDB5alhV0iat/Projet-R%C3%A9seau?node-id=0%3A1)

# Sujet:

## I-Les systemes automnomes
Chaque groupe est responsable de la mise en oeuvre d'un AS. Cette mise en oeuvre doit respecter le cahier des charges suivant. Tout élément on  précisé est à la discretion du groupe. En ce qui concerne vos choix, ils devront être justifiés dans votre rapport.

### CAHIER DES CHARGES pour l'AS 0
- L'AS O est un fournisseur de service réseau parmi lesquels un service d'accès Internet au particulier, un service d'accè Internet au réseau d'entreprise ou encore un service DNS.
- L'AS utilise un protocole de routage dynamique.
- L'AS propose une solution d'interconnexion sans configuration pour ses clients particuliers.
- Les clients de l'AS 0 sont:
  - Un site d'entreprise primaire géré par le groupe 0
  - Un site d'entreprise secondaire géré par le groupe 1
  - Un particulier du groupe 0
  - Un particulier du groupe 2
- L'AS détient la plage d'adresse 120.0.16\*x.0/20 et attribue les plages d'adresses de ses clients dans cet espace.
### Accès d'un particulier
- Accès de type box-like
- A terme ce particulier devera être capable d'accéder au réseau d'entreprise
### Accès des entreprises
- Permettre l'accès à deux sites de deux entreprises 
- Mettre en place de la QOS pour les entreprises
- 
## II-L'interconnexion des sytèmes autonomes
Les trois groupes doivent mettre en place l'interconnexion de leur AS.

### CAHIER DES CHARGES
- A la discrétion des étudiants.

## III-Les réseaux d'entreprise
### CAHIER DES CHARGES
- **Mise en oeuvre du site principal de l'entreprise**
  - mise en place du réseau et du service d'adressage dynamique,
  - mise en place d'une sécurité d'accès au réseau en interne,
  - mettre en place le DNS de l'entreprise,
  - mettre en place un service de VoIP,
  - mettre en place au minimum un autre service applicatif  de votre choix

- **Mise en oeuvre du site secondaire de l'entreprise
  - mise en place du site secondaire
  - mise en place d'un VPN entre les sites

- **Accès d'un particulier**
  - offrir un accès sécurisé à un particulier à son site d'entreprise

