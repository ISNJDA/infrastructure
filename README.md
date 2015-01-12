# Introduction

Le but des exercices travaux pratiques consiste à préparer les composants de la visionneuse. Afin de pouvoir lire des médias et aussi créer une visionneuse fonctionnelle, il faut :

* Pouvoir détecter tous les fichiers présents dans un dossier.
* Comprendre le contenu des fichiers afin de savoir comment les jouer (vidéo, audio, application web).
* Collecter des métadonnées sur ces fichiers afin de pouvoir afficher des informations complémentaires (la durée de la vidéo ou du segment audio, le nom de son auteur, sa date etc...).
* Agréger toutes ces informations dans un format facilement exploitable pour plus tard.
* Déclencher la lecture des fichiers automatiquement.

Au cours de ces exercices nous allons donc construire un prototype complet.

# Préparation

Vous devez vous assurer que les bibliothèques suivantes sont disponibles sur votre environnement Python :
* PyUnit - un framework de test unitaire, que vous allez utiliser pour valider vos exercices.
* Hachoir - la bibliothèque de métadonnées multimédia.
* DBus - la bibliothèque de communication avec les applications Linux.
* VLC - pour la lecture de médias.
* Gpicview - pour la lecture d'images.
* Subversion - pour télécharger les exercices depuis Github.

Sous Debian / Ubuntu / Raspbian, vous pouvez exécuter les commandes suivantes :

```shell
sudo apt-get install python-unit python-hachoir-core python-hachoir-metadata python-hachoir-parser python-dbus subversion vlc gpicview
```

# Obtenir les exercices

Les exercices sont disponibles librement sur Github, avec la commande suivante :

```shell
svn export https://github.com/ISNJDA/infrastructure/trunk/travaux_pratiques
```

Vous avez ensuite un fichier **Visionneuse.py**, un dossier **medias** et un fichier **TestVisionneuse.py**.

Vous pouvez immédiatement faire tourner les tests avec :

```shell
python -m unittest -f TestVisionneuse
```

Les tests vont bien entendu tous échouer, car le code n'est pas encore écrit.
Il faut maintenant compléter les fonctions du fichier **Visionneuse.py** afin de faire passer tous les tests unitaires.

Une fois le fichier **Visionneuse.py** complété, vous aurez une visionneuse qui détecte automatiquement les fichiers et les lit.

Veuillez vous référer aux TP correspondants dans le wiki pour vous aider à compléter les exercices.

* [Wiki](https://github.com/ISNJDA/infrastructure/wiki)
* [TP systèmes de fichier](https://github.com/ISNJDA/infrastructure/wiki/TP-syst%C3%A8mes-de-fichier)
* [TP métadonnées et types MIME](https://github.com/ISNJDA/infrastructure/wiki/TP-m%C3%A9tadonn%C3%A9es-et-types-MIME)
* [TP sur la lecture de média et DBUS](https://github.com/ISNJDA/infrastructure/wiki/TP-sur-la-lecture-de-m%C3%A9dia-et-DBUS)
* [TP sur les formats de données textuels](https://github.com/ISNJDA/infrastructure/wiki/TP-sur-les-formats-de-donn%C3%A9es-textuels)
* [TP d'introduction sur Kivy](https://github.com/ISNJDA/infrastructure/wiki/TP-d%27introduction-sur-Kivy)



