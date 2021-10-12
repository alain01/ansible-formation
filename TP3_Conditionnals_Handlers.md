# TP Playbook handlers

> Le But de ce TP est de d'utiliser les variables ansible, les conditionnals et les handlers

URL :

https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html

https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html

https://docs.ansible.com/ansible/latest/user_guide/playbooks_vars_facts.html

https://docs.ansible.com/ansible/latest/user_guide/playbooks_handlers.html

https://docs.ansible.com/ansible/latest/collections/ansible/builtin/lineinfile_module.html

https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html

https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_module.html

https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html

## BUT : management SSH server : cas d'usage 

 - 1. Installation / vérif d'install 
 - 2. Configuration
 - 3. Démarrage ou redémarrage d'un service

### Création d'un nouveau playbook :

> Créer le fichier  manage_ssh.yaml

1) Déclarer des variables

    - Créer les variable ci-dessous pour déclarer lnécessaires à l'écosysteme OpenSSH server

       ```yaml
       debian_ssh_package: openssh-server
       redhat_ssh_package: openssh-server
       ssh_service: sshd
       custom_sshd: true
       ```

2) S'assurer que le produit openssh-server est installé sur les machines distantes

    > Utiliser les modules **apt** et **yum** dédiés aux distributions plutôt que simplement **package**.

    > Il faudra sans doute utiliser une condition pour déclencher les module sur le bon périmètre

    > Tips : when, facts (os_family)

3) Utiliser le module **lineinfile** pour modifier une ou plusieurs lignes dans un fichier et seulement (condition when ) en fonction de la variable **custom_sshd**

   -  Modifier la configuration du serveur openssh (/etc/ssh/sshd_config): (module lineinfile) => loop pour 2 modif

      - modif 1:
      ```yaml
      path: /etc/ssh/sshd_config
      regexp: '^#?LogLevel .*'
      line: "LogLevel DEBUG"
      ```
      - modif 2: 
      ```yaml
      regexp: '^#?X11Forwarding .*'
      line: "X11Forwarding no"
      ```

    > /!\ ATTENTION en cas de mauvaise syntaxe (le service ssh ne redémarre pas): penser au paramètres validate et backup


4) On souhaite redémarrer le service sshd si modification de config 

- Si modification (changed) =>appeler un handlers pour redémarrer le service ssh

> TIPS : https://docs.ansible.com/ansible/latest/user_guide/playbooks_handlers.html