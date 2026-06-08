# [:es:](README.md) [:de:](README_DE.md) [:uk:](README_EN.md)
# Export to Web - GIMP 3.0 Plugin

Optimisez vos images pour le web en un seul clic ! **Export to Web** est un plugin développé en Python pour **GIMP 3.0** qui automatise le processus de compression, de redimensionnement et de préparation des images pour garantir qu'elles pèsent moins de 2 Mo et se chargent rapidement sur n'importe quel site web.

## 🚀 Fonctionnalités

Le plugin exécute automatiquement les tâches suivantes sur l'image active :
1. **Aplatir l'image :** Fusionne tous les calques visibles en un seul calque d'arrière-plan.
2. **Redimensionnement intelligent :** Si la hauteur de l'image dépasse `3000px`, le plugin la réduit proportionnellement pour éviter des fichiers excessivement lourds.
3. **Ajustement de la résolution :** Modifie la résolution de l'image à `72 DPI` (le standard pour les écrans web).
4. **Exportation optimisée (.jpg) :** Enregistre le fichier au format JPEG avec une qualité de `80%`, un encodage progressif et un sous-échantillonnage 4:4:4 pour maintenir un équilibre parfait entre le poids du fichier et la fidélité visuelle.

### 📁 Destination du fichier :
* Si l'image d'origine **a déjà été enregistrée**, le plugin générera le fichier `.jpg` optimisé dans le **même dossier** avec le même nom.
* S'il s'agit d'une **nouvelle image sans titre**, elle sera automatiquement exportée sur votre **Bureau** sous le nom `web_export.jpg`.

---

## 🛠️ Configuration requise

* **GIMP 3.0** (ou version supérieure) avec prise en charge des plugins Python 3.
* Bibliothèques système d'introspection d'objets GNOME (`PyGObject`, `Gio`, `Gimp 3.0`).

---

## 🔧 Installation

Pour installer le plugin, suivez ces étapes :

1. **Téléchargez ou copiez** le fichier du script et nommez-le (par exemple : `export_web.py`).
2. Rendez le fichier **exécutable**.
   * *Sur Linux/macOS :* Ouvrez un terminal et exécutez `chmod +x export_web.py`.
3. **Déplacez le fichier** dans votre répertoire de plug-ins GIMP 3.0 :
   * **Linux :** `~/.config/GIMP/3.0/plug-ins/`
   * **Windows :** `%APPDATA%\GIMP\3.0\plug-ins\`
   * **macOS :** `~/Library/Application Support/GIMP/3.0/plug-ins/`

> 💡 **Note pour GIMP 3.0 :** GIMP exige souvent que les plugins soient placés dans un dossier portant exactement le même nom que le script (par exemple, un dossier nommé `export_web` contenant le fichier `export_web.py`).

4. Redémarrez GIMP.

---

## 📖 Mode d'emploi

Une fois correctement installé, vous trouverez le plugin directement dans la barre de menus de GIMP :

Allez dans : **Fichier** > **Exporter** > **Export to web**

Le processus s'exécutera en arrière-plan (mode non interactif) pour vous éviter des clics inutiles.

---

## ✍️ Auteurs

* **Développeurs :** Sergio Maya López
* **Année :** 2026

---

## 📄 Licence

Ce projet est sous Licence Publique Générale GNU (GPLv3). N'hésitez pas à le modifier, le distribuer et l'adapter à vos besoins.
