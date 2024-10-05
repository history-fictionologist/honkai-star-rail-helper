# honkai-star-rail-helper

`honkai-star-rail-helper` est un utilitaire conçu pour gérer et traiter les données des personnages, les compétences et les recommandations de reliques pour le jeu vidéo [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail). Il lit les fichiers d'entrée, traite diverses attributs tels que les informations des personnages et les ensembles de compétences, et génère les résultats dans un format organisé. Les données d'entrée proviennent des packages de mise à jour officiels dans le dépôt [StarRailData](https://github.com/Dimbreath/StarRailData/tree/master) et les résultats sont stockés dans des dossiers spécifiques à chaque version pour une gestion facile.

## Dernière Table des Personnages
<!-- CHARACTER_TABLE_START -->
|            |   | La Destruction                        | La Chasse       | L'Érudition | L'Harmonie                | La Nihilité    | La Préservation           | L'Abondance |
| ---------- | - | ------------------------------------- | --------------- | ----------- | ------------------------- | -------------- | ------------------------- | ----------- |
| Physique   | 5 | Clara\|Yunli\|{M#Pionnier}{F#Pionnière} | Le Fossoyeur    | Argenti     | Robin                     |                |                           |             |
| Physique   | 4 |                                       | Sushang         |             | Hanya                     | Luka           |                           | Natasha     |
| Feu        | 5 | Luciole                               | Topaz et Compti | Himeko      |                           | Jiaoqiu        | {M#Pionnier}{F#Pionnière} | Lingsha     |
| Feu        | 4 | Hook                                  |                 |             | Asta                      | Guinaifen      |                           | Gallagher   |
| Glace      | 5 | Jingliu                               | Yanqing         |             | Ruan Mei                  |                | Gepard                    |             |
| Glace      | 4 | Micha                                 |                 | Herta       |                           | Pela           | March 7th                 |             |
| Foudre     | 5 |                                       |                 | Jing Yuan   |                           | Achéron\|Kafka |                           | Bailu       |
| Foudre     | 4 | Arlan                                 | Moze            | Serval      | Tingyun                   |                |                           |             |
| Vent       | 5 | Blade                                 | Feixiao         |             | Bronya                    | Cygne noir     |                           | Huohuo      |
| Vent       | 4 |                                       | Dan Heng        |             |                           | Sampo          |                           |             |
| Quantique  | 5 |                                       | Seele           | Jade        | Sparkle                   | Louve d'argent | Fu Xuan                   |             |
| Quantique  | 4 | Xueyi                                 |                 | Qingque     |                           |                |                           | Lynx        |
| Imaginaire | 5 | Dan Heng • Imbibitor Lunae            | Dr Ratio        |             | {M#Pionnier}{F#Pionnière} | Welt           | Aventurine                | Luocha      |
| Imaginaire | 4 |                                       | March 7th       |             | Yukong                    |                |                           |             |
<!-- CHARACTER_TABLE_END -->

## Fonctionnalités Clés
- Télécharge automatiquement les données des personnages, les CV, les ensembles de compétences et les recommandations de reliques.
- Traite et organise les données dans des répertoires d'entrée/sortie spécifiques à chaque version.
- Configuration des numéros de version via la ligne de commande pour chaque nouvelle mise à jour.

## Prérequis

Assurez-vous d'avoir les éléments suivants :
- **Python 3.8+** (confirmez avec `python3 --version`).
- Les paquets Python requis sont listés dans `requirements.txt`.

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(Optionnel) Créer et activer un environnement virtuel :**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scriptsctivate
   ```

3. **Installer les dépendances (aucune dépendance supplémentaire n'est actuellement requise) :**
   ```bash
   # Pas besoin d'installer de dépendances pour le moment, mais si nécessaire à l'avenir :
   # pip install -r requirements.txt
   ```

## Utilisation

### Exécuter l'outil
   Naviguez vers le répertoire `src/` et exécutez le script principal avec le numéro de version souhaité :
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - Remplacez `<version_number>` par la version actuelle (par exemple, `2.5`).
   - Si vous souhaitez ignorer le téléchargement des fichiers, ajoutez l'option `--skip-download`.

   Les fichiers d'entrée seront téléchargés dans le dossier `input/{version}` et les résultats seront enregistrés dans le dossier `output/{version}`.

### Exemple d'Utilisation

- Pour exécuter le script avec la version `2.5` et télécharger les fichiers :
  ```bash
  python3 main.py --version 2.5
  ```

- Pour exécuter le script avec la version `2.5` et ignorer le téléchargement des fichiers :
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- Pour exécuter le script avec la version 2.5 et télécharger les fichiers pour des langues spécifiques (par exemple, EN et JP) :
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## Contribuer

Nous accueillons les contributions ! Vous pouvez :
- Soumettre une pull request pour de nouvelles fonctionnalités ou des corrections de bugs.
- Signaler tout problème via le système de suivi des problèmes.
- Assurez-vous que toutes les contributions incluent des tests et une documentation pertinente.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.
