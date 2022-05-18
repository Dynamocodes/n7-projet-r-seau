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
- L'AS utilise un protocole de routage dynamique. commits 
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

- **Mise en oeuvre du site secondaire de l'entreprise**
  - mise en place du site secondaire
  - mise en place d'un VPN entre les sites

- **Accès d'un particulier**
  - offrir un accès sécurisé à un particulier à son site d'entreprise

## Objectifs du projet
A travers ce projet, nous vous proposons d'illustrer une partie de de vos connaissances réseaux, principalement sur les technologies IP. Ce projet impose certaines contraintes sutout matérielles, notamment au niveau des équipements disponibles dans les salles. Toutefois, l'essantiel des points reste précédents. Même si la partie système informatique peut y avoir une part importante (comme souvent dans la mise en place de réseau), l'objectif principal est la mise en place d'une architecture réseau, la mise en oeuvre de **protocoles**, la **compréhension** de la leur fonctionnement et leurs **observations**. Dans cette optique un rapport et une démo seront les points clé de votre évaluation.

Le thème du projet est double : la mise en œuvre d'un réseau 'entreprise multi-sites et la mise en place
assez minimaliste d'un AS et de son interconnexion avec d'autres AS.

## Oraganisation et déroulement des séances

Le projet sera mené par 4 groupes différents. La répartition du travail devra être équilibrée entre tous les
membres de l'équipe, chacun devant connaître les différentes solutions présentées dans le cadre du projet.

Le travail se découpera en un travail individuel, un travail par groupe et un travail de l'ensemble de la
promotion.

Le projet n'a pu être concentré sur une semaine donc veillez à utiliser au maximum votre machine pour
sauvegarder votre travail. A la fin de la dernière journée, 2h seront utilisées pour la présentation de votre
travail, les deux heures précédentes étant dédiées à la préparation des salles.

## Evaluation
Le travail sera évalué à partir de trois éléments:
- L'implication de chaque étudiant et sa motivation à apporter des solutions. Cette partie sera évaluée
par son propre groupe par un bilan à la fin du rapport. Il ne s'agit pas de faire de la délation mais
d'être honnête sur les apports de chacun pour pouvoir avancer au mieux lors d'un projet. A cette fin,
un chef de projet sera désigné par le groupe et évaluera les autres membres du groupe. De la même
façon les autres membres du groupe évalueront leur chef de projet. Au début de chaque demi-journée,
le chef de projet fera un point après de l'encadrant présent dans la salle.
- La démonstration finale de vote projet. Il s'agit là d'une présentation dont vous êtes responsables
entièrement. La première demi-heure sera consacrée à l'interconnexion des AS, puis chaque groupe
aura 15 minutes pour présenter son travail. Cinq petites minutes seront laissées pour poser des
questions si besoin et gérer le battement. C'est à vous de préparer le planning, la démonstration et les
interventions.
- Un rapport (un pour chaque groupe) qui devra contenir vos principaux choix, vos observations et un
guideline de la mise en place de votre architecture réseau.
