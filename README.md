# Django Formation

(Lien git du projet)[https://github.com/lance-kawa/django_formation]


Ce projet est un support de cours pour les formations Django que je réalise.
Vous pouvez le lancer en mode production de cette façon:

`cp .env.local .env`

Modifier alors vos variables d'environnement pour correspondre à la configuration de votre projet/de votre serveur.
Attention `PGHOST=127.0.0.1` ne fonctionne que si vous lancez votre projet avec runserver ou gunicorn sans docker
En utilisant Docker vous devez précisez le nom du conteneur qui contient votre base de donnée (ici `postgres_faunatrack`)

## Commandes django courantes 

 - `python manage.py runserver` lance votre projet en mode development
 - `python manage.py showmigrations` Voir les migrations appliquées/non appliquées
 - `python manage.py makemigrations` Génère les fichiers de migrations
 - `python manage.py makemigrations {app_label} --empty` Génère une migration vide
 - `python manage.py migrate` Applique les migrations sur la base de données
 - `python manage.py migrate {app_label} XXXX` Revenir à la migration XXXX
 - `python manage.py migrate {app_label} zero` Revenir à une base de données vides de toutes les migrations liés à notre application {app_label}
 - `python manage.py show_urls` Affiche la liste des urls de votre projet et leur correspondance littérale pour pouvoir les reverse_lazy (nécessite django-extensions)
 - `python manage.py shell` Lance un shell python qui a accès à votre projet/ votre base de donnée
 - `python manage.py collectstatic --no-input` Génère vos fichiers statiques (pour le passage en production)
 - `python manage.py makemessages -l fr_FR` Génère un fichier .po pour les traductions
 - `python manage.py compilemessages` Génère un fichier .mo pour appliquer vos traductions
...

## Commandes docker et docker compose courantes :

- `docker ps` liste vos conteneurs actifs
- `docker ps -a` liste vos conteneurs actifs et inactifs
- `docker compose ps` liste vos conteneurs du fichier docker-compose.yml du répertoire courant
- `docker compose up` Lance la commande run pour chacun de vos conteneurs du fichier docker-compose.yml du répertoire courant
- `docker compose up -d` Pareil en mode détaché
- `docker compose up --build` pour build de nouveaus vos conteneurs (suite à une modification d'un fichier par exemple)
- `docker compose build --no-cache` pour build de vos conteneurs sans utiliser le cache (parfois utile)
- `docker compose down` Stop vos conteneurs et les supprime (ne supprime pas les volumes associés !)
- `docker volumes ls` Liste vos volumes
- `docker system prune` Supprime les volumes, images et conteneurs non utilisés seulement (pratique pour libérer de l'espace et de la RAM)


## Installer Docker

- Package obligatoire (normallement déjà installé)
`sudo apt-get install apt-transport-https ca-certificates curl software-properties-common`

- Clé docker
`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

- Ajouter le repo de docker 
`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`

- Installer docker-ce
`sudo apt-get install docker-ce`

## Lien utiles 

- GitHub Formatteur: https://github.com/orgs/lance-kawa/repositories
- Documentations Django: https://docs.djangoproject.com/fr/5.0/
- ORM Django : (Query)[https://docs.djangoproject.com/fr/5.0/topics/db/queries/], (API)[https://docs.djangoproject.com/fr/5.0/ref/models/querysets]
- Tailwind : https://tailwindcss.com/docs/container






