
# Bienvenue dans PasswordBuster.

## Comment l'utiliser ?

### Utilisation basique :

Ajouter vos wordlists en .txt dans le dossier "dicos"

Ouvrer le fichier config.json.

Pour chaque dictionnaire, un objet de la forme suivate doit être ajouté :

`{"name": "noms",
      "functions":
      [
        {"initiale" : true},
        {"toUpper": true}
      ]}`

(Note : vous pouvez copié celui de l'exemple pour conserver le formatage exact)

Indiquer ensuite par "true" ou "false" si la fonction doit être appliquée au dictionnaire ou non.

Lancer ensuite le main.py.

Renseigner le nom du fichier de sortie souhaité.

Patienter ...

Le fichier de sortie est disponible dans le dossier sorties_txt

### Ajouter une fonction

Pour ajouter un nouvelle fonction de traitement des mots, créer la fonction dans le fichier functions.py.
Un prototype de fonction est disponible.

Modifier ensuite le fichier config.json pour rajouter l'option d'utilisation de cette fonction pour chaque dictionnaire.

`{"name": "noms",
      "functions":
      [
        {"initiale" : true},
        {"toUpper": true},
        {"NOUVELLE_FONCTION": true},
      ]}`

Enfin, se rendre dans le main.py pour rajouter les deux lignes suivantes, à la ligne 41.

            if dic_fonctions['NOUVELLE_FONCTION']:
                new_dico.append(f.NOUVELLE_FONCTION(c_dico))