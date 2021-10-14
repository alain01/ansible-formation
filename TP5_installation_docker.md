# Utilisation d'un role docker externe pour installer le produit sur notre maquette

## Preparer l'utilisation du rôle

1. Créer un fichier requirement.yaml dans le répertoire role
2. Installer le role dans notre projet : ansible-galaxy

   ```bash
   $ ansible-galaxy role install -r roles/requirements.yml -p roles/
   ```

## Creation d'un playbook pour installer docker

1. Creer un groupe dans l'inventaire : docker pour y positionner srv01

2. Creer un playbook avec :

    ```yaml
    hosts: docker
    ```

    - appel du role docker

## Test install 

- En mode Ad-Hoc on vérifie la version de docker sur le groupe docker 

```bash
$ ansible -m shell -a "docker version" docker -b
```


## Test de modules ansible docker 

- Avec des modules fournis par ansible, déployer un conteneur sur la machine distante
  - Ajouter dans le playbook, une task qui cree un conteneur

     - nom de conteneur
     - image : nginx:1.21-alpine