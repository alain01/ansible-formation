# TP creation role Apache

## Exemple PLAYBOOK 

```yaml
---
- hosts: ansiblecli
  remote_user: ansible
  become: true
  vars:
    service: httpd
    package: httpd
    admin: formtion@ansible.lan

  tasks:
  - name: install apache
    yum:
      name: "{{ package }}"
      state: latest
  - name: demarre apache
    systemd:
      name: "{{ service }}"
      state: started
  - name: modifie le serveradmin
    lineinfile:
      path: /etc/httpd/conf/httpd.conf
      regexp: '^ServerAdmin'
      line: "{{ admin }}"
    notify:
      - redemarre apache
  handlers:
    - name: redemarre apache
      systemd:
        name: "{{ service }}"
        state: restarted
```

## Transformation en rôle

- 1. Initialiser le rôle

- 2. Définir les variables

- 3. Definir les handlers

- 4. Définir les tasks


## Appel du rôle dans un playbook

- 1. Creer un playbook de déploiement du rôle

   - /!\ Si vous suivez l'exemple des modules, ce rôle ne peut être déclenché que sur du RedHat/Centos 
   - Pensez dans le play à filtre le hosts sur srv02

- 2. Déclencher !!!!


## Améliorer le role pour qu'il puisse installer apache sur famille RedHat et Debian

  - Penser à une nouvelle de faire :
  
    - include_tasks

       - Dans le répertoire tasks : un main.yaml qui peut appeler d'autres fichiers yaml
        
          ```yaml
          include_tasks: "{{ ansible_facts['os_family'].yaml }}"
          ```


