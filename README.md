# User guide
## Présentation du projet
Ce projet porte sur les Diagnostics de Performance Energétique (DPE) en France. Il est composé de deux histogrammes et d'une carte de la France.\
Un histogramme montre les émissions de Gaz à effet de Serre en fonction de l'année de construction des foyers. Et le deuxième montre la consommation énergétique en fonction de l'année de construction des foyers.\
Pour la carte de la France il y a des points de différentes couleurs (couleurs qui décrit la classe consommation du foyer).

Les données sont disponibles sur le site https://www.data.gouv.fr/fr/datasets/dpe-logements-avant-juillet-2021/ .

## Installation
Pour installer le projet sur votre machine personnelle, en vous plaçant dans la zone de travail que vous voulez, il vous suffit de taper l'instruction : \
`$ git clone https://github.com/DOMESDAY7/dashboard_dpe.git]`

Ce projet utilise des packages dont voici la liste : 
+ colorama version 0.4.6
+ dash version 2.7.0
+ pandas version 1.5.0
+ plotly version 5.10.0
+ requests version 2.28.1

Après l'installation du projet sur votre machine, pour que le projet fonctionne, il vous faut installer les packages additionnels qui se trouvent dans le requirements.txt. Pour ce faire il vous faut utiliser l'instruction suivante : \
`$ python -m pip install -r requirements.txt`

## Démarrage
En vous plaçant dans le projet, c'est-à-dire ./dashboard_dpe dans le cas où vous n'avez pas changé le nom du projet sur votre machine, vous pouvez lancer le programme en utilisant l'instruction : \
`$ python main.py`

Ensuite il vous aller à l'adresse indiquée dans un navigateur, dans notre cas il s'agit de http://127.0.0.1:8050/.

## Utilisation
Sur cette page web, vous pouvez visionner deux histogrammes, une carte de la France, ainsi qu'une FAQ qui répond aux questions potentielles de l'utilisateur. 

Pour chaque histogramme, vous avez des boutons qui permttent de définir à partir de quelle année de construction l'histogramme commence et un slider qui permet de définit la dernière année de l'intervalle. A partir de ces deux paramètres les histogrammes sont mis à jour. 

Pour la carte de France, en plaçant votre curseur sur la carte vous pouvez zoomer/ dézoomer avec la molette. Vous pouvez aussi cliquer sur les classes de consommation d'énergie que vous voulez voir ou non.

```mermaid
flowchart LR;
  WEB_DASHBOARD-->MAIN;
  MAIN-->Controller_Histogramme;
  MAIN-->Controller_DPE_map;
  MAIN-->FAQ-->questionsAnswers;
  Dataset-->get_data;
  Controller_Histogramme-->model_histogramme;
  Controller_Histogramme-->model_histogramme2;
  get_data-->Controller_Histogramme;
  model_histogramme-->get_histo;
  model_histogramme2-->get_histo2;
  Controller_DPE_map-->model_dpe_map;
  get_data-->Controller_DPE_map;
  model_dpe_map-->get_map;
```