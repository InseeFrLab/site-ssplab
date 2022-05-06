# Site internet du SSP Lab

Ce repository contient le code permettant de déployer un site de type blog sur un cluster Kubernetes déjà configuré, sur le modèle du site du SSP Lab de l'Insee (https://ssplab.lab.sspcloud.fr/).

## Instructions

Pour déployer le site Internet, il faut suivre les étapes suivantes :
- Dans le contrat Kubernetes `kubernetes/deployment.yaml`, spécifier le lien vers le repository Docker Hub qui contiendra l'image de l'application Django. Ce lien doit correspondre au lien donné dans l'étape `Docker meta` du build Github workflow (`.github/workflows/main.yml`). Les credentials Docker Hub doivent être correctement entrés comme secrets sur le repository Github ;
- Une clé secrète (https://docs.djangoproject.com/en/dev/ref/settings/#secret-key) unique pour chaque installation de Django doit être spécifiée dans un secret Kubernetes, grâce à la commande
```
kubectl create secret generic django-secret --from-literal=key=<your-key>
```
- Le nom de domaine est spécifié dans le contrat `kubernetes/ingress.yaml` ;
- Pour pouvoir accéder à l'interface administrateur de Django (au travers de laquelle on modifie le contenu disponible sur le site), il faut disposer d'une autorisation. Pour créer un compte administrateur, ouvrir un shell dans le conteneur en cours d'exécution :
```
kubectl exec -it site-ssplab-xxxxx -- /bin/sh
```
puis lancer la commande suivante :
```
DJANGO_SUPERUSER_PASSWORD=<admin-password> python3 manage.py createsuperuser \
    --no-input \
    --username=<admin-username> \
    --email=<admin-email>
```
