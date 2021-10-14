# Utilisation d'un role docker externe pour installer le produit sur notre maquette

## Preparer l'utilisation du rôle

1. Créer un fichier requirement.yaml dans le répertoire role
2. Installer le role dans notre projet : ansible-galaxy

## Creation d'un playbook pour installer docker

1. Creer un groupe dans l'inventaire : docker pour y positionner srv01

2. Creer un playbook avec :

    ```yaml
    hosts: docker
    ```

    - appel du role docker