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

- 2. Déclencher !!!!


