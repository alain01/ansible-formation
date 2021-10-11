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