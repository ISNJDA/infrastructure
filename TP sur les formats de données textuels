# Introduction

JSON ("djaisone") et YAML ("yameul") sont deux formats de données textuels.
Les données textuelles sont des données qui sont à la fois lisibles par un ordinateur et par un être humain. Elles sont structurées afin d’être facilement exploitables par un ordinateur, mais elles peuvent être éditées dans un éditeur de texte. A l'inverse de données binaires (telles celles contenues dans une image JPEG ou un document PDF), elles peuvent être créées et exploitées très simplement.

# JSON

JSON signifie "Notation Objet JavaScript" (JavaScript Object Notation). Un document JSON représente des données hiérarchiques qui associent un nom avec une valeur.

Par exemple si on voulait stocker des données sur une personne, on pourrait creer le document JSON suivant:

```json
{ 
  "nom" : "Mandela",
  "prenom" : "Nelson",
  "dateDeNaissance" : "18-07-1918"
}
```

On obtient donc un objet *personne* qui contient les attributs *nom*, *prenom*, *dateDeNaissance*.

On peut lire des données JSON grace au package Python **json** comme dans l'exemple suivant :
```python
import json 

mandelaJson = """
{ 
  "nom" : "Mandela",
  "prenom" : "Nelson",
  "dateDeNaissance" : "18-07-1918"
}
"""

mandelaObjet = json.loads(mandelaJson)

print(mandelaObjet['prenom'] + " "+ mandelaObjet['nom'].upper() 
       + " (" +mandelaObjet['dateDeNaissance']+")")
```

On peut aussi ajouter des objets supplémentaires à l’intérieur de cet objet, par exemple, les enfants de cette personne :

```python
import json 

mandelaJson = """
{ 
  "nom" : "Mandela",
  "prenom" : "Nelson",
  "dateDeNaissance" : "18-07-1918",
  "enfants" : [
     { 
       "nom" : "Mandela",
       "prenom" : "Madiba Thembekile",
       "dateDeNaissance" : "23-02-1945"
     }
    ,{ 
       "nom" : "Mandela",
       "prenom" : "Makgatho",
       "dateDeNaissance" : "26-06-1950"
     }
  ]
}
"""

mandelaObjet = json.loads(mandelaJson)

print(mandelaObjet['prenom'] + " "+ mandelaObjet['nom'].upper() 
    + " (" +mandelaObjet['dateDeNaissance']+")")

for enfant in mandelaObjet['enfants']:
    print("  - "+enfant['prenom'] + " "+ enfant['nom'].upper() 
       + " (" +enfant['dateDeNaissance']+")") 
```


# YAML

YAML est un autre format de données textuel, similaire à JSON mais plus compact simple à lire. Par contre, contrairement a JSON qui peut être exploité directement par un navigateur Web (car JSON est en fait du JavaScript simplifié), YAML demande d'utiliser des fonctions spécifiques.

Pour reprendre notre exemple précédent, en YAML notre personne exemple ressemblerait à :

```yaml
nom : mandela
prenom : nelson
dateDeNaissance : 18-07-1918
enfants:
   - nom : Mandela
     prenom : Madiba Thembekile
     dateDeNaissance : 23-02-1945
   - nom : Mandela
     prenom : Makgatho
     dateDeNaissance : 26-06-1950
```

et le script Python affichant ces donnees serait :

```python
import yaml

mandelaYaml = """
nom : mandela
prenom : nelson
dateDeNaissance : 18-07-1918
enfants:
   - nom : Mandela
     prenom : Madiba Thembekile
     dateDeNaissance : 23-02-1945
   - nom : Mandela
     prenom : Makgatho
     dateDeNaissance : 26-06-1950
"""

mandelaObjet = yaml.load(mandelaYaml)

print(mandelaObjet['prenom'] + " "+ mandelaObjet['nom'].upper() 
    + " (" +mandelaObjet['dateDeNaissance']+")")

for enfant in mandelaObjet['enfants']:
    print("  - "+enfant['prenom'] + " "+ enfant['nom'].upper() 
       + " (" +enfant['dateDeNaissance']+")")
```
On appelle le package **yaml** au lieu du package **json** et la fonction **load()** - mais le code python affichant les données reste le même.

:warning: Si la bibliothèque YAML n'est pas présente, il peut être nécessaire de l'installer avec :

```shell
sudo apt-get install python3-yaml
```

# Conclusion

Le JSON et le YAML sont deux formats de données textuels très répandus à la fois sur Internet et dans le monde de la programmation.
