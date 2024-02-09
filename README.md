# Django Formation

Ce projet est un support de cours pour les formations Django que je réalise.
Vous pouvez le lancer en mode production de cette façon:

`cp .env.local .env`

Modifier alors vos variables d'environnement pour correspondre à la configuration de votre projet/de votre serveur.
Attention `PGHOST=127.0.0.1` ne fonctionne que si vous lancez votre projet avec runserver ou gunicorn sans docker
En utilisant Docker vous devez précisez le nom du conteneur qui contient votre base de donnée (ici `postgres_faunatrack`)

## Commandes django courantes 

`python manage.py runserver` lance votre projet en mode development
`python manage.py makemigrations` génère les fichiers de migrations
`python manage.py migrate` Applique les migrations sur la base de données
`python manage.py showmigrations` Voir les migrations appliquées/non appliquées
`python manage.py showm_urls` Affiche la liste des urls de votre projet et leur correspondance littérale pour pouvoir les reverse_lazy (nécessite django-extensions)
`python manage.py shell` Lance un shell python qui a accès à votre projet/ votre base de donnée
`python manage.py makemigrations {app_label} --empty` Génère une migration vide
`python manage.py collectstatic --no-input` Génère vos fichiers statiques (pour le passage en production)
`python manage.py makemessages -l fr_FR` Génère un fichier .po pour les traductions
`python manage.py compilemessages` Génère un fichier .mo pour appliquer vos traductions
...

## Commandes docker et docker compose courantes :

`docker ps` liste vos conteneurs actifs
`docker ps -a` liste vos conteneurs actifs et inactifs
`docker compose ps` liste vos conteneurs du fichier docker-compose.yml du répertoire courant
`docker compose up` Lance la commande run pour chacun de vos conteneurs du fichier docker-compose.yml du répertoire courant
`docker compose up -d` Pareil en mode détaché
`docker compose up --build` pour build de nouveaus vos conteneurs (suite à une modification d'un fichier par exemple)
`docker compose build --no-cache` pour build de vos conteneurs sans utiliser le cache (parfois utile)
`docker compose down` Stop vos conteneurs et les supprime (ne supprime pas les volumes associés !)
`docker volumes ls` Liste vos volumes
`docker system prune` Supprime les volumes, images et conteneurs non utilisés seulement (pratique pour libérer de l'espace et de la RAM)






