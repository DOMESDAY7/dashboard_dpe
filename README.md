# User guide
## Présentation du projet
Ce projet porte sur les Diagnostics de Performance Energétique (DPE) en France. Il est composé de deux histogrammes et d'une carte de la France.\
Un histogramme montre les émissions de Gaz à effet de Serre en fonction de l'année de construction des foyers. Puis le deuxième montre la consommation énergétique en fonction de l'année de construction des foyers.\
Pour la carte de la France il y a des points de différentes couleurs (couleurs qui décrit la classe consommation d'énergie du foyer).

Les données sont disponibles sur le site https://www.data.gouv.fr/fr/datasets/dpe-logements-avant-juillet-2021/ .

## Installation
Pour installer le projet sur votre machine personnelle, en vous plaçant dans la zone de travail que vous voulez, il vous suffit de taper l'instruction : \
`$ git clone https://github.com/DOMESDAY7/dashboard_dpe`

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

Ensuite il vous suffit d'aller à l'adresse indiquée dans un navigateur, dans notre cas il s'agit de http://127.0.0.1:8050/.

## Utilisation
Sur cette page web, vous pouvez visionner deux histogrammes, une carte de la France, ainsi qu'une FAQ qui répond aux questions potentielles de l'utilisateur. 

Pour chaque histogramme, vous avez un slider qui permet de définir l'intervalle d'année. A partir de ces deux paramètres(année de début et année de fin), les histogrammes sont mis à jour automatiquement. 

Pour la carte de France, en plaçant votre curseur sur la carte vous pouvez zoomer/ dézoomer avec la molette. Vous pouvez aussi cliquer sur les classes de consommation d'énergie que vous voulez voir ou non.

## Architecture du code
Dans notre architecture, nous nous sommes inspirés de l'architecture MVC (Model View Controller).
### Synthèse des fichiers
```mermaid
flowchart LR;
  WEB_DASHBOARD-->MAIN;
  MAIN & Dataset-->Controller_Histogramme & Controller_DPE_map;
  MAIN-->FAQ-->questionsAnswers.json;
  Controller_Histogramme-->model_histogramme_average_energie & model_histogramme_average_GES;
  Controller_DPE_map-->model_dpe_map;
```
### Avec les interactions
```mermaid
classDiagram
  App<|--Controller_histogramme
  Dataset<|-- Controller_dpe_map
  Dataset<|-- Controller_histogramme
  App<|-- Controller_dpe_map
  Controller_dpe_map<|-- DpeMap
  Controller_histogramme<|--Histogramme_average_GES
  Controller_histogramme<|--Histogramme_average_energie
  App:+callback()
  App:+int begin_year_energie
  App:+int end_year_energie
  App:+int begin_year_GES
  App:+int end_year_GES
  App:+sliders_value
  App: +histo
  App: +histo2
  class Controller_histogramme{
    +update()
    +int begin_year_energie
    +int end_year_energie
    +int begin_year_GES
    +int end_year_GES
    +Histogramme_average_energie
    +Histogramme_average_GES
  }
  class Histogramme_average_GES{
    +init()
    +get_histo()
    +data
    +int begin_year
    +int end_year
  }
  class Histogramme_average_energie{
    +init()
    +get_histo()
    +data
    +int begin_year
    +int end_year
  }
  class Dataset{
    +init()
    +get_data()
    +get_fields()
    +getSize()
    +getSelect()
    +getSort()
    +getFieldValue()
    +get_dataframe()
    +dumpURL()
    +String URL_BASE
  }
  class DpeMap{
    +init()
    +get_map()
    +data
  }
  class Controller_dpe_map{
    +data
    +figmap
    +DpeMap()
    +data
  }
```

## Conclusion 
On peut voir que plus les foyers ont été construits il y a longtemps plus la consommation énergétique et le taux d'émissions de gaz à effet de serre sont élevés, donc dû notamment à l'isolation. Il faut donc isoler les vieux bâtiments car ce sont les moins isolés.


# Developper guide
Nous avons donc utilisé une architecture avec Model View Controller, View est ici le fichier main. Ce fichier va faire appelle dans la fonction callback aux différents controllers pour mettre à jour ici les histogrammes en fonction des valeurs des sliders.

Chaque fichier controller récupère la data que l'on veut avec le constructeur de Dataset. Pour faire un histogramme sur une autre donnée, il faudrait changer le paramètre de get_data dans le modèle changer ainsi que le nom que recherche les dictionnaires. De même pour la map.

Les fichiers model récupèrent la data en brut et stockent en fonction des noms de data dans certains dictionnaires.
Ces classes ont deux fonction une init et une get_map/get_histo qui retourne juste la map ou l'histogramme.

## Copyright
Je déclare sur l’honneur que le code fourni a été produit par moi/nous même, à l’exception des lignes ci dessous.

Pour chaque ligne (ou groupe de lignes) empruntée, donner la référence de la source et une explication de la syntaxe utilisée.

Toute ligne non déclarée est réputée être produite par l’auteur (ou les auteurs) du projet. L’absence ou l’omission de déclaration sera considéré comme du plagiat.
