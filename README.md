# 🎮 Projet : Pierre – Feuille – Ciseaux

Un petit jeu classique **Pierre – Feuille – Ciseaux** développé en **Python**, avec une structure modulaire et un affichage coloré dans le terminal.

---

## 🧩 Objectif du projet

Le but est de créer un jeu interactif où :
- Le joueur choisit entre **pierre**, **feuille** ou **ciseaux**  
- L’ordinateur choisit aléatoirement une option  
- Le programme détermine le gagnant selon les règles classiques :
  - 🪨 Pierre bat Ciseaux  
  - 📄 Feuille bat Pierre  
  - ✂️ Ciseaux bat Feuille  
  - 💥 Égalité si les choix sont identiques  

---

## 🕹️ Comment y jouer ?
1. **Lance le jeu**
   — Ouvre ton terminal à la racine du projet et exécute : `python main.py`.
2. **Menu principal**
   — Tape `1` pour lancer une partie, `2` pour quitter.
3. **Joue ton coup** — Pendant la partie, choisis :
   `1` = 🪨 Pierre,
   `2` = 📄 Feuille,
   `3` = ✂️ Ciseaux.
L'ordinateur choisit aléatoirement et le résultat s'affiche à l'écran.
4. **Continuer ?**
    — À la fin de la manche, tape `y` pour rejouer ou `n` pour quitter. Bonne partie !
   
---

## 🗂️ Arborescence du projet

``````
Projet-Pierre-Feuille-Ciseaux/
│
├── src/
│ ├── game_directory/
│ │ └── game.py # Contient la logique principale du jeu
│ │
│ ├── start/
│ │ └── begining.py # Menu de démarrage et lancement de la partie
│ │
│ ├── state/
│ │ └── var.py # Variables globales (scores, états du jeu)
│ │
│ └── main.py # Point d’entrée principal du programme
│
├── .gitignore
├── LICENSE
└── README.md
``````
