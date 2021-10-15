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

---

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

- Methode via un virtualenv python

   - 1. Mecanique python : creer un virtualenv

       ```bash
       $  sudo apt install python3-virtualenv
       ```
    
   - 2. A ma demande : activer le virtualenv

       ```bash
       $ source ~/venv_ansible_2.9.10/bin/activate
       ```

   - 3. Dans ce virtual actif on install des packages PIP : ansible

      ```bash
      $ pip3 install ansible==2.9.10
      $ source ~/venv_ansible_2.9.10/bin/activate
      ```
  
  - 4. Test du binaire
      
      ```bash
      $ ansible --version
      ```

  - 5. Sortir du virtualenv

     ```bash
     $ deactivate
     ```

---

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


## Configuration environnement ansible - ansible.cfg

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

  > hostvars[] et groups[] => interroger des variables pour un node précis ou lister le contenu d'un groupe de l'inventaire

- Facts : variables/nodes récoltées automatiquement lors du déclenchement de la task module setup

  > https://docs.ansible.com/ansible/latest/user_guide/playbooks_vars_facts.html#ansible-facts


- Precedence des variables 

  > https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable

  - Déclarer une même variable dans plusieurs fichiers ET avec des valeurs différentes
  - Notion de poids : précedence/surcharge
  - Adapter le code a des contextes différents simplement en redéclarant une variable à l'endroit désiré


- Facts

  - données recoltées sur chaque machine via le module ansible.builtin.setup
  - Dans un playbook, une task "gather facts" est déclenchée automatiquement
  - On peut désactiver la task auto : 
      ```yaml
      gather_facts: false
      ```
  - On peut utiliser une mécanique de cache pour les facts

     > https://docs.ansible.com/ansible/latest/plugins/cache.html


## Boucles - loop - with_item

- Itération sur des structures de données type liste et dictionnaire.
- Permet de ne créer qu'une task dans le playbook et traiter plusieurs élements


> https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html

> https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html#iterating-over-a-dictionary


## Gestion des données sensibles :

- Ansible vault

> https://docs.ansible.com/ansible/latest/user_guide/vault.html
> https://docs.ansible.com/ansible/latest/user_guide/vault.html#managing-vault-passwords

- Commande :

  ```bash
  $ ansible-vault --help
  ```

- Ex 1 méthode online :

  - 1. Demande d'encryption d'une string (mot de passe)
    
      ```bash
      $ ansible-vault encrypt_string 'formation123' --name 'password'
      ```

      - /!\ : le mot de passe demande sert à encrypter ET decrypter, il est saisi à la volée et non conservé !!!

  - 2. Copie du retour de la commande dans le playbook

  - 3. Déclenchement du playbook en ajout l'option **--ask-vault-password** et ainsi saisir le mot de passe vault pour décrypter

     ```bash
     $ ansible-playbook requirement.yaml --ask-vault-password
     ```

- Méthode fichier à plat : --vault-password-file

- Méthode script avec outils tier pour aller cherche le mot de passe 

   > https://github.com/alibaba/ansible-provider-docs/blob/master/contrib/vault/vault-keyring-client.py


- Commandes sur fichier :

   ```bash
  $ ansible-vault encrypt requirement.yaml
  $ ansible-vault decrypt requirement.yaml
  $ ansible-vault encrypt requirement.yaml
  $ ansible-vault edit requirement.yaml 
  $ ansible-vault --he
  $ ansible-vault view  requirement.yaml
  ```


## Conditionnals

- Déclencher une task sur condition

  > https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html

- Permet d'orienter le déroulement du play et des tasks

## Handlers

- Déclencher une task sur changement

  > https://docs.ansible.com/ansible/latest/user_guide/playbooks_handlers.html


## Block

- Regroupement logique de task, permet d'y associer des condition et variables (simplifie, reduit le code)
- Implementation de rescue et always

> https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html

> CF demo_block_rescue.yaml

## Template Jinja

- Gérer des fichiers dynamiques (avec variables)
- Permet d'adapter le contenu d'un fichier par rapport à un contexte, des variables

- CF : playbook demo_template_jinja2.yaml

  > https://docs.ansible.com/ansible/latest/user_guide/playbooks_templating.html

  > https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html


## Syntax check et dry-run

- Vérification syntaxe :

   ```bash
   $ ansible-playbook demo_template_jinja2.yaml --syntax-check
   ```
  
- Mode dry-run, preview

  ```bash
  $ ansible-playbook demo_template_jinja2.yaml --check
  ```

- Mode dry-run + visu changements sur files ou templates

  ``back
  $ ansible-playbook demo_template_jinja2.yaml --check --diff
  ```


## ROLES

- Ensemble d'actions coordonnées pour réaliser un ensemble cohérent (installer nginx et le configurer etc)
- Un rôle est par defaut autonome et a son propre cycle de vie (versionning)
- organisé en différents outils (tasks, templates, handlers, variables (default ou non), meta)
- sert à être partagé et réutilisé dans l'entreprise, dans le hub galaxy

- Creation d'un skelete de role :

  ```bash
  $ ansible-galaxy init --init-path roles/ ansible_role_ssh
  ```

> https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html


- Utilisation de roles communautaires

  - Les rôles ont leur propre cycle de vie, independants du cycle de vie du projet ansible (des repos git différents)
  - On liste les rôles nécessaire à notre projet dans un fichier requirements.yml
  - On télécharge les rôles avec la commande : ```$ ansible-galaxy role install -r requirements.yml```

    ```bash
    $ ansible-galaxy role install -r roles/requirements.yml -p roles/
    ```

    > https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file


## Optimisation du déroulement

> https://docs.ansible.com/ansible/latest/user_guide/playbooks_async.html
> https://docs.ansible.com/ansible/latest/user_guide/playbooks_strategies.html

- delegate_to : controller où est déclenché une tasks 
  > https://docs.ansible.com/ansible/latest/user_guide/playbooks_delegation.html


## Conception de modules

  - CF répertoire library et demo_mymodule.yaml

  - https://docs.ansible.com/ansible/latest/dev_guide/developing_modules.html#developing-modules



## AWX - TOWER

- Ansible GUI

- S'installe sur un environnement dédié, n'impact pas le fonctionnement ansible cli. 

- Se base sur les dépôts git

- Peut être utilisé en parallele de ansible cli

- Permet de déleguer des taches, visualiser, creer des workflow, sheduler

> https://github.com/ansible/awx/blob/devel/INSTALL.md

> https://github.com/ansible/awx-operator

  - 1. Création des crédentials (source control git, ssh)
  - 2. Creation d'un projet (synchroniser le depot git)
  - 3. Synchro de l'inventaire (lire l'inventaire)
  - 4. Creation de templates/workflow (preparer le déclenchement des playbook)


## Inventaire dynamique

> https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html
> https://github.com/ansible-collections/community.general/tree/main/plugins/inventory

- Ex vsphere :

  >  https://docs.ansible.com/ansible/latest/scenario_guides/vmware_scenarios/vmware_inventory.html

- Methode script

    > https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html#developing-inventory-scripts

    - script d'interrogation CMDB/provider
    - Générer une output format JSON qui sera interpretée par ansible
    - https://github.com/irongomme/ansible_ovh_public_cloud/blob/master/ovh_public_cloud.py

- Essayer de trouver des exemples de scripts (cloud, vmware)

- De plus en plus de plugin via les collection ansible

  > https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_inventory.html