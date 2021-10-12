# TP Playbook et variables

> Le But de ce TP est de découvrir et utiliser les variables ansible. Pour cela, un playbook recensera l'appel des modules via des tasks et utilisera des variables de diverses structures

Url :
https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html

https://docs.ansible.com/ansible/latest/collections/ansible/builtin/debug_module.html


-----
## Exercice 1

**Affichage d’une variable globale/facts**

- Dans un nouveau playbook **requirements.yml**, s'adressant à la pattern/target/hosts *all*, utiliser le module **debug** permettant d’afficher le nom de la distribution de la cible ainsi que sa version majeure, en utilisant des variables globales nommées facts.

    * Pour trouver la variable globale à utiliser le mode "Ad-Hoc"
        ```bash
        $ ansible -m setup -i hosts all | grep "distribution"
        ```
    
    * Pour afficher des variables, utiliser le module **debug**

## Exercice 2

**Utilisation d’une variable locale**

- Dans le playbook **requirements.yml**, créer une variable locale de type liste nommée *liste_packages* contenant 3 elements : 
  - vim
  - nano
  - curl
  
- Utiliser cette variable dans le module **package** comme valeur du parametre name. Cela permettra de demander l'installation des packages (éléments dans la liste sur les machines distantes). Penser au become pour élévation de privilèges



## Exercice 3

**Utilisation d’une variable locale de type liste**

- Déclarer la variables :

   ```yaml
   liste_user:
     - formation
     - dev01
     - deploy01
    ```

- Utiliser le module user pour créer les trois utilisateur
    - /!\ cela devrait coincer

> Il va falloir aborder la notion de loop (boucles)

  - https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html