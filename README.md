# Export Français dans le Monde: 2018

## Description de la base de donnée

Lien des datas originales:
https://data.economie.gouv.fr/explore/dataset/donnees-du-commerce-exterieur-visualisation/table/?disjunctive.arborescence_nc8_simplifiee&disjunctive.label_fr

Description de la base de donnée après traitement:

- Pays: Nom des pays classés par ordre alphabétique.
- Mois: Mois de l'année en chiffre pour un export.
- Valeurs: Apport monétaire en euros(€) de l'export.
- Masse: Volume en kilogramme(Kg) de l'export.
- Longitude: Coordonnée géographique du pays sur la longitude.
- Latitude: Coordonnée géographique du pays sur la latitude.

## Python
## Installation des packages

- pip install dash
- pip install plotly
- pip install pandas
- pip install numpy

csv devrait être inclu dans Python, et plotly.express dans plotly. Si toutefois vous rencontrez un problème:
- pip install nom_du_package

## Utilisation du script

Assurez vous que les fichiers suivants soient dans le même dossier:

- assets
- data.csv
- script.py

Le temps de traitement de la base de données étant assez long (plus d'1 million de ligne à traiter), il est fourni le dataset déjà traité:

- new_data.csv

Pour tester la partie traitement de données du script.py, supprimez/déplacez simplement new_data.csv.

Pour Python nous allons devoir rentrer une commande dans un terminal.
Il est recommandé d'utiliser VisualStudio code:
- Ouvrez VisualStudio Code.
- Cliquez sur File puis sur Open Folder.
- Selectionnez le dossier dans lequel vous avez placé les précédents fichiers.
- Cliquez sur Terminal puis New Terminal.
- Pour Linux: tapez python3 main.py pour lancer le script.
- Pour Windows: tapez la commande: python main.py pour lancer le script.

A la fin de l'éxécution du script, l'adresse http://127.0.0.1:8050/ est renvoyée. Utilisez cette adresse pour visualiser le DashBoard.
Si le dashboard affiche des erreurs, rafraichissez la page du navigateur. Si les problèmes persistent, relancez le script.

## R
## Installation des packages

Pour l'installation des packages, il est recommendé de décommenté dans R studio les 7 premières lignes du fichier export_projet.R.
Ignorez les messages pop up en cliquant sur "Non" lorsque vous lancerez l'Application.
Une fois que vous aurez lancer une première fois l'Application, vous pouvez recommenter les lignes afin d'éviter les messages pop up.

Toutefois vous pouvez retrouver les commandes d'installation:
- install.packages('shiny')
- install.packages("shinydashboard")
- install.packages("plotly")
- install.packages("ggplot2")
- install.packages("dplyr")
- install.packages("leaflet")
- install.packages("reticulate")

## Utilisation du script

Assurez vous que les fichiers suivant soient dans le même dossier:

- .RData
- .Rhistory
- data.csv
- export_projet.R
- export_projet.Rproj
- server.R
- ui.R
- sort_script.py

Le temps de traitement de la base de données étant assez long (plus d'1 million de ligne à traiter), il est fourni le dataset déjà traité:

- new_data.csv

Pour tester la partie traitement de données du sort_script.py, supprimez/déplacez simplement new_data.csv.

Pour R:
- Ouvrez RStudio.
- Cliquez sur File puis Open Project.
- Selectionnez export_projet.Rproj dans le dossier où vous avez placé les précédents fichiers.
- Dans la fenêtre Files en bas à droit de RStudio: séléctionnez export_projet.R.
- Cliquez sur "Run App".

Une fenêtre RStudio devrait s'ouvrir avec le Shiny DashBoard, toutefois si elle ne s'afficher pas vous pouvez taper l'adresse visible dans le terminal sur un navigateur internet: http://127.0.0.1:3572.

## Guide d'extention du code.
## Python

Le script Python est découpé en 3 grandes parties.
- Traitement de données: le traitement du csv est contenu dans une fonction create_new_set(), une extension de cette fonction peut être facilement effectué afin d'effectuer les modifications voulues au data_set original.
Dans le cas de notre étude, la fonction permet de se débarasser des lignes contenant des valeurs non définies (NaN), sommer les colonnes Valeurs et Masse pour chaque Pays pour chaque Mois et enfin réorganiser un nouveau
data_set rangé par ordre alphabétique, et par ordre de mois pour chaque Pays.
- Création du DashBoard: ce morceau de code contient l'architecture du DashBoard sur la page navigateur et l'interface utilisateur. Les commentaires dans le code permettent de détailler les différentes divisions html. Le dernier commentaire donne des indications afin d'étendre le code et ajouter d'autres éléments au DashBoard. Enfin, un fichier style.css est contenu dans le dossier ./assets de ce projet, il permet de faciliter la mise en page et l'ésthétique du DashBoard. Le ficher est facilement extensible pour les adeptes du css.
- Callback,Graphiques et interactivité: dernière partie qui regroupe la logique et les fonctions permettant l'interaction de l'utilisateur avec le DashBoard. Ce code gère la logique des sliders,dropdowns et autres inputs.
Les différentes fonctions associées aux callbacks s'occupent de la création et l'update des différents éléments graphiques du DashBoard.

## R

Le projet R contient 4 script.
- sort_script.py: ce script python est responsable du traitement des données. Il est basé sur une architecture similaire à la fonction du script du projet Python et peut donc être modifié/étendu très facilement. Celui-ci retourne un nouveau csv nommé: new_data.csv. Ce script est directement appelé lorsque l'on lance l'application R par le fichier export_projet.R.
- export_projet.R: le fichier principal du projet qui permet de lancer l'application. Ce fichier appelle le script python de traitement de donnée seulement si new_data.csv n'est pas présent dans le dossier du projet. Dans le cas contraire, il ouvre le data_set traité et lance l'application Shiny Dash. Il est aussi résponsable de la mise en place des librairies et contient les instructions d'installation de package qui peuvent être décommentées comme précisé dans la partie Utilisation du script. Il est recommendé de ne pas étendre ce code avec de la logique serveur ou des éléments d'interfaces dashboard mais seulement des variables de style ou d'ordre général.
- server.R: ficher contenant la logique des différents graphiques. Il s'occupe du rendu des graphiques de manière dynamique en prenant en compte les différentes Input venant de l'interface utilisateur. C'est aussi ce fichier qui se charge du titre des graphiques, des couleurs, des axes et autres paramètres. Pour étendre le code, les outputs doivent concorder avec les éléments de ui.R qui leurs sont associées. Hormis pour les données géolocalisées, ce code utilise la librairie plotly, il faut donc bien s'assurer t'utiliser la méthode renderPlotly lorsque l'on effectue l'affectation d'une output. Si vous souhaitez utiliser une autre librairie (Leaflet,ggplot2,...) assurez vous d'utiliser le render propre à cette librairie afin d'éviter une erreur de rendu.
- ui.R: fichier s'occupant de l'interface et l'agencement des différents éléments calculés par server.R sur le dashBoard. Une sidebar est présente afin de choisir entre les valeurs monétaires ou les volumes, il est possible d'ajouter d'autres items à cette sidebar en respectant l'architecture du code actuel. Pensez à rajouter un tabItem dans la variable body si vous ajouter une option dans la sidebar, attention à bien concorder l'ID de l'option avec le tabItem. Vous pouvez ensuite écrire le code des nouveaux éléments graphiques dans votre tabItem. Pour les éléments graphiques, n'oubliez pas de développer la partie logique dans server.R en faisant concorder l'ID des éléments graphiques avec vos Outputs et Inputs de la partie server.R. Ecrivez vos extentions seulement dans les variables sidebar et body, l'instruction shinyUI permet justement de joindre les 2 variables.
Comme pour la partie serveur, assurez vous d'utiliser la méthode d'Output spécifique au package de l'élément graphique que vous souhaitez afficher, par exemple plotlyOutput pour plotly.

## Principales conclusions de l'étude

Le but de l'étude est de mettre en relief certaines caractéristiques de l’export mondial français.

- D’après les valeurs monétaires, on estime une très faible variation des exports français dans le monde. Ainsi les pays continuent à investir dans le marché français sans impact flagrante sur la situation actuelle. Les acteurs principaux de ces échanges sont l’Allemagne, les États Unis, l’Espagne et l’Italie. En faisant varier l’échelle du nombre par tranche de valeurs (en euros) des exports, on visualise une disparité conséquente. En effet, d’après l’histogramme on a uniquement 8 pays qui investissent entre 40M et 50M (en euros) dans l’export français pour 88 pays qui investissent entre 0 et 10M (euros). Donc l’export français s’appuie sur de gros investisseurs mondiaux mais aussi sur des pays qui ont des intérêts financiers moins importants avec la France.
- Les quantités d’exports (en Kg), reste elles aussi assez semblable. On l’explique par la forte demande sur le marché français pouvant être gérer via les nombreux ports internationaux qu’elle possède.  Cette fois si les principaux pays importateurs de produits français en termes de volumes sont, la Belgique, l’Allemagne, l’Espagne et l’Italie (dans l’ordre décroissant). On estime en s’appuyant sur ces éléments mais aussi sur la carte mondiale que le principal facteur de ces exports français se situe via le billet de l’Europe.
