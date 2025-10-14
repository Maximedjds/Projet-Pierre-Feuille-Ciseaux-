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
   — Tape `1` pour lancer une partie, `2` pour lancer la version graphique, `3` pour quitter.
3. **Joue ton coup** ( version terminal)
   — Pendant la partie, choisis :
   `1` = 🪨 Pierre,
   `2` = 📄 Feuille,
   `3` = ✂️ Ciseaux.
L'ordinateur choisit aléatoirement et le résultat s'affiche à l'écran.
5. **Continuer ?**
    — À la fin de la manche, tape `y` pour rejouer ou `n` pour quitter. Bonne partie !
1
   
---

## 🐍✨ Explication des fichiers Python

---

### 🕹️ **`game.py`** — *Gestion de la partie*
> Contient toute la logique principale du jeu 🎮  

📜 **Fonctionnalités principales :**  
- 🔁 Boucle principale du jeu  
- 👤 Gestion des entrées du joueur et de l’ordinateur  
- 🏆 Gestion des victoires, défaites et du score  

---

### 🚀 **`begining.py`** — *Lancement de la partie*
> Responsable du démarrage du jeu et de la navigation dans le menu 🧭  

📜 **Fonctionnalités principales :**  
- 🏠 Affichage du menu d’accueil  
- ▶️ Lancement de la boucle principale du jeu  

---

### ⚙️ **`var.py`** — *Gestion des variables*
> Centralise toutes les variables globales pour une meilleure organisation 🧩  

📜 **Fonctionnalités principales :**  
- 🧠 Stockage des variables globales  
- 🛠️ Facilite la modification et la maintenance du code  

---

### 🧩 **`main.py`** — *Point d’entrée du programme*
> Fichier principal qui exécute le jeu 💥

---

## 🎨 Partie Graphique du Jeu

---

### 🖥️ `graphic/game.py`
> Gère toute la version **graphique et interactive** du jeu 🕹️  

📜 **Fonctionnalités principales :**  
- 🎬 Affichage des différents écrans (menu, jeu, résultat)  
- 🖱️ Gestion des événements et interactions (clics, retours, transitions)  
- 🔊 Lecture des **sons de clic** et **musique de fond**  
- 🌈 Rendu visuel dynamique avec images et animations  

🎵 **Musique de fond :**  

- 🎵 Une musique d’ambiance est jouée automatiquement pendant la partie. 
---

### 🖱️ `graphic/bouton.py`

📜 **Fonctionnalités principales :**  
- 🧭 Création et gestion des boutons (textes ou images)
- ✨ Effets visuels de survol et animation de clic
- 🔊 Lecture du son de clic pour un retour sonore immédiat
- ⚙️ Liaison directe avec les actions du jeu (navigation, choix, etc.)

💡 C’est le moteur d’interaction entre le joueur et l’interface graphique.

---
    
## 🗂️ Arborescence du projet

``````
📁 Projet-Pierre-Feuille-Ciseaux
│
├── 📂 assets
│   ├── 📂 fonts
│   │   └── 🅰️ NFPixels-Regular.ttf
│   │
│   ├── 📂 images
│   │   ├── 📂 computer
│   │   │   ├── 🖼️ Ciseaux.png
│   │   │   ├── 🖼️ Feuille.png
│   │   │   └── 🖼️ Pierre.png
│   │   │
│   │   ├── 📂 player
│   │   │   ├── 🖼️ Ciseaux.png
│   │   │   ├── 🖼️ Feuille.png
│   │   │   └── 🖼️ Pierre.png
│   │   │
│   │   ├── 🖼️ bg.png
│   │   ├── 🖼️ bg_game.png
│   │   ├── 🖼️ icon.png
│   │   ├── 🖼️ paper.png
│   │   ├── 🖼️ rock.png
│   │   └── 🖼️ scissors.png
│   │
│   └── 📂 son
│       ├── 🔊 mixkit-arcade-game-jump-coin-216.wav
│       ├── 🔊 mixkit-arcade-retro-game-over-213.wav
│       ├── 🔊 mixkit-huge-crowd-cheering-victory-462.wav
│       ├── 🔊 mixkit-sci-fi-click-900.wav
│       └── 🎵 mixkit-tech-house-vibes-130.mp3
│
├── 📂 src
│   ├── 📂 game_directory
│   │   ├── 📂 graphic
│   │   │   ├── 🐍 button.py
│   │   │   └── 🐍 game.py
│   │   └── 🐍 game.py
│   │
│   ├── 📂 start
│   │   └── 🐍 begining.py
│   │
│   └── 📂 state
│       └── 🐍 var.py
│
├── ⚙️ .gitignore
├── 📜 LICENSE
├── 🐍 main.py
└── 📘 README.md

``````
