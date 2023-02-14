Prérequis :
-
Il faut avoir Cmake installé et le dossier \bin de Cmake ajouté au path. 
Prévoyez aussi un compilateur c++ (gcc) et verifiez sa detection par Cmake (ajout au path).

Procesus d'import (windows) : 
-
NB : Il faut avoir visual studio (vscode ne remplace pas) installé ! + on se place à la racine du projet dans ce qui suit pour commencer.

- pip install Cmake (posssibe redondance)
- pip install numpy
- cd .\mon_pybind\
- rmdir .\pybind11 
- git clone https://github.com/pybind/pybind11
- cd ..
- pip install .\mon_pybind\


Procesus d'import (linux) :
-
NB : on se place à la racine du projet pour commencer dans ce qui suit.

- pip install Cmake (possible redondance)
- pip install numpy
- cd mon_pybind
- rm -r pybind11
- git clone https://github.com/pybind/pybind11
- mkdir build
- cd build
- cmake ..
- make
- cd ..
- python setup.py bdist_wheel

verifiez la création d'un dossier dist et de son contenu en .wlh

- pip install dist/(fichier.wlh)

Vérifications :
-
Dans les deux cas verifez l'installation par un "pip freeze" qui affiche les module installés, ou par un "import shufflerModule" dans un fichier ou terminal python.