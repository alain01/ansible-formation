# Formation Ansible

## Vagrant

> /!\ BIen se positionner dans le répertoire où est situé Vagrantfile

```bash
$ vagrant up
$ vagrant status
$ vagrant ssh master.formation.lan
```

## Intro

- Projet Opensource 2012
- Racheté par RedHat en 2015 - 2 version CE / Enterprise

> https://github.com/ansible/ansible

- Infra As Code - déploiement de configuration/conformité - installations produits/déploiements - administration réseau/providers/virtualisation

> https://www.ansible.com/

- Doc : 
  - https://docs.ansible.com/ansible/latest/index.html
  - https://www.redhat.com/files/summit/session-assets/2017/S100812-miller.pdf
  - http://people.redhat.com/mlessard/mtl/presentations/apr2018/AnsibleF5WorkshopVF.pdf
  - https://ansible.github.io/workshops/decks/ansible_best_practices.pdf



## Installations

- Controler node : prérequis python >= 2.7
- Managed node : prérequis >=2.6

- Méthodes : gestionnaire package OS, sources, ***PIP**

> /!\ Bien lire la doc sur les release et choisir sa version :  https://docs.ansible.com/ansible/devel/reference_appendices/release_and_maintenance.html


- Méthode via PIP :

```bash
$ sudo apt update && sudo  apt install -y python3-pip
$ pip3 install ansible
$ . ~/.profile
$ ansible --version
```

## Concepts et notion de base ansible 

* Control/manager/management node :
  - noeud disposant de ansible (binaire) et permettant de déployer
  - accès ssh aux autres machines (bastions...)
  - password ou clef ssh
  - interpréteur Python
  - sécurité importante
  - VirtualEnv python pour déployer le binaire Ansible

* Managed nodes :
  - serveurs cibles
  - permet la connexion ssh
  - élévation de privilèges via le user ( SUDO => audit)
  - interpréteur Python

* Inventaire/Inventory :
  - inventaires des machines (ip, dns)
  - format ini (plat) ou format yaml
     - et les variables, surcharge de variable (host_vars et group_vars)
     - statique (fichiers) ou dynamique (api via script)
  - utilisation de patterns possible (srv-prd-[0-15])
         > Règles de nommage des hostname/DNS
     - Groupes : 
  	   * dans un inventaire les machines peuvent être regroupées (serveur web, databases...)
  	   * possibilité de créer différents niveaux > arbre (parents/enfants)
  	   * groupe racine = all

* Module :
  - Code python qui réalise une action ciblée sur une technologie (gestion des users, gestion de fichier, gestion de clés)
  - Un module prend des options/arguments/paramètres => /!\ certain arguments sont requis, d'autres ont des valeurs par défaut


## Configuration environnement ansible 

> ansible-config

```bash
$ ansible-config view
$ ansible-config list
```

- Fichiers de configuration ansible ou variable d'environnement

  > https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html
  > https://github.com/ansible/ansible/blob/stable-2.11/examples/ansible.cfg


## Inventaire - Inventory

- FIchier plat ini ou yaml

- commande : ansible-inventory

```bash
$ ansible-inventory -i /vagrant/hosts --list
$ ansible-inventory -i /vagrant/hosts --list --yaml
$ ansible-inventory -i /vagrant/hosts --graph
```

## Ansible - mode Ad-Hoc

> Mécanisme d'idempotence qui entre en jeux : 
> On décrit un état désiré au travers et de ses options
> Le code exécuté à distance, analyse et réalise l'action uniquement si nécessaire. 
> Plusieurs status : CHANGED, SUCCESS, FAILED

- Commande : ansible et ansible-doc

- Documentation et list des modules

   ```bash
   $ ansible-doc -l
   $ ansible-doc ping
   ```

- Premier test avec le module ping :

```bash
$ ansible --help
$ ansible -i hosts -m ping srv01
$ ansible -i hosts -m ping
$ ansible -i hosts -m ping all --private-key ~/.ssh/id_ed25519
```

- Appel d'un module avec arguments

```bash
$ ansible -i hosts -m user -a "name=formation" all
```

- Appel d'un module avec argument et élévation de privilèges:


-K, --ask-become-pass
                        ask for privilege escalation password
  -b, --become          run operations with become (does not imply password prompting)


```bash
$ ansible -i hosts -m user -a "name=formation comment=formation" all --become --ask-become-pass
```

- Idempotence : état désiré

```bash
$ ansible -i hosts -m user -a "name=formation comment=formation state=absent" all -b -K
```

- Commandes one-shot

```bash
$ ansible -i hosts -a "free -m" all
$ ansible -i hosts -m shell -a date all
```


## Playbook :


> fichier déclenchant les actions à réaliser

> sert à articuler l'inventory avec les rôles

> peut inclure des tasks (actions), des variables

> peut faire tout ce que fait un rôle (globalement) 

>  spécifier quel user et comment ?

> spécifier besoin tel que élévation de privilèges


> Beaucoup d'options possibles au lancement

  ```bash
  $ ansible-playbook --help
  ```

  * -i : inventory
  * -l : limit > spécifier un/des groupes ou serveurs ou patterns
  * -u : user
  * -b : become > sudo
  * -k : password de ssh (à éviter)
  * -K : password du sudo
  * -C : check > dry run
  * -D : diff > afficher les différences avant/après les tasks (actions)
  * --ask-vault : prompt pour le password vault
  * --syntax-check : vérfier la syntax
  * --vault-password-file : passer le vault password par un fichier
  * -e : surcharger n'importe quelle variable
  * -f : nombre de parallélisation
  * -t : filtrer sur les tags (--skip-tags)
  * --flush-cache : éviter l'utilisation du cache
  * --step : une tâche à la fois (confirmation via prompt)
  * --start-at-task : commencer à une tâche spécifiquement
  * --list-tags : lister tous les tags rencontrés
  * --list-tasks : liste les tâches qui vont être exécutées

```bash
$ ansible-playbook -i hosts --become premier-playbook.yaml
```


## Fonction/Plugins :

> https://docs.ansible.com/ansible/latest/plugins/lookup.html


## Variables - Specials Variables - Faits/Facts

- Variables déclarées manuellement

  > https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html

- Magic vars : auto

  > https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html

- Facts : variables/nodes récoltées automatiquement lors du déclenchement de la task module setup

  > https://docs.ansible.com/ansible/latest/user_guide/playbooks_vars_facts.html#ansible-facts