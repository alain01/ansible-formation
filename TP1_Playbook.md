# TP Playbook

> Le But de ce TP est de découvrir et utiliser un ensemble de modules Ansible. Pour cela, un playbook recensera l'appel des modules via des tasks et s'adressera à un host (debian)

- Urls :
    - https://docs.ansible.com/ansible/latest/collections/ansible/builtin/user_module.html
    - https://docs.ansible.com/ansible/latest/collections/ansible/posix/authorized_key_module.html
    - https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html
    - https://docs.ansible.com/ansible/latest/collections/ansible/builtin/group_module.html

## Création du playbook :

> Créer dans votre répertoire projet ansible, un playbook nommé bootstrap.yml

1) Déclarer le PLAY en le nommant :
    ```yml
    - name: PLAY bootstrap
    ```

2) Donner la *target* du play :
   ```yml
   hosts: srv01
   ```

3) A l'aide du module **ping**, vérifier la connectivité avec le node distant (prérequis)

4) A l'aide du module **group**, créer un groupe **ansible** avec les paramètres suivants :
    - nom : ansible
    - état : présent
    - gid : 2000

5) A l'aide du module **user**, créer un utilisateur **ansible** avec les paramètres suivants :
    - nom : ansible
    - état : présent
    - shell : /bin/bash
    - uid : 2000
    - gid : 2000

6) A l'aide du module **authorized_key** ajouter la clé publique locale au projet ansible nommée **id_ed25519.pub** pour le user ansible nouvellement créé
   - user: ansible
   - état: présent
   - clé: => lookup (recherche un fichier local depuis le master)

7) A l'aide du module **copy**, générer un nouveau fichier sur le node distant nommé **/etc/sudoers.d/ansible**. Paramètres :
    - destination : /etc/sudoers.d/ansible
    - contenu : 'ansible ALL=(ALL:ALL) ALL'
    - backup
    - propriétaire : root
    - group : root
    - mode : 0440
    - validation : /usr/sbin/visudo -csf %s

    > /!\ Bien regarder tous les paramètres dispo pour ce module.
    Penser donc à demander un backup du fichier et un test de syntax avant déploiement pour éviter une corruption SUDO

8) Déclencher le playbook à l'aide de la commande **ansible-playbook**, attention les actions nécessitent une élévation de privilège, donc à répercuter dans la commande dans un premier temps.

    > L'aide : ansible-playbook --help