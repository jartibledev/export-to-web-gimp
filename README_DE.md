# [:es:](README.md) [:fr:](README_FR.md) [:uk:](README_EN.md) 
# Export to Web - GIMP 3.0 Plugin

Optimieren Sie Ihre Bilder für das Web mit nur einem Klick! **Export to Web** ist ein in Python entwickeltes Plugin für **GIMP 3.0**, das das Komprimieren, Ändern der Größe und Vorbereiten von Bildern automatisiert, damit sie unter 2 MB bleiben und auf jeder Website schnell geladen werden.

## 🚀 Funktionen

Das Plugin führt automatisch die folgenden Aufgaben für das aktive Bild aus:
1. **Bild zusammenfügen (Flatten):** Vereint alle sichtbaren Ebenen zu einer einzigen Hintergrundebene.
2. **Intelligente Skalierung:** Wenn die Bildhöhe `3000px` überschreitet, wird das Bild proportional verkleinert, um übergroße Dateien zu vermeiden.
3. **Auflösung anpassen:** Ändert die Bildauflösung auf `72 DPI` (der Standard für Bildschirme).
4. **Optimierter Export (.jpg):** Speichert die Datei im JPEG-Format mit einer Qualität von `80%`, progressiver Kodierung und 4:4:4-Farbunterabtastung (Sub-sampling), um eine perfekte Balance zwischen Dateigröße und Bildqualität zu gewährleisten.

### 📁 Speicherort der Datei:
* Wenn das Originalbild **bereits gespeichert wurde**, erstellt das Plugin die optimierte `.jpg`-Datei im **gleichen Ordner** unter demselben Namen.
* Wenn es sich um ein **neues Bild ohne Titel** handelt, wird es automatisch auf Ihrem **Desktop** unter dem Namen `web_export.jpg` gespeichert.

---

## 🛠️ Anforderungen

* **GIMP 3.0** (oder höher) mit Unterstützung für Python 3-Plugins.
* GNOME Object Introspection Systembibliotheken (`PyGObject`, `Gio`, `Gimp 3.0`).

---

## 🔧 Installation

Um das Plugin zu installieren, folgen Sie diesen Schritten:

1. **Laden Sie die Skriptdatei herunter** oder kopieren Sie sie und benennen Sie sie (z. B. `export_web.py`).
2. Machen Sie die Datei **ausführbar**.
   * *Unter Linux/macOS:* Öffnen Sie ein Terminal und führen Sie `chmod +x export_web.py` aus.
3. **Verschieben Sie die Datei** in Ihr GIMP 3.0 Plug-ins-Verzeichnis:
   * **Linux:** `~/.config/GIMP/3.0/plug-ins/`
   * **Windows:** `%APPDATA%\GIMP\3.0\plug-ins\`
   * **macOS:** `~/Library/Application Support/GIMP/3.0/plug-ins/`

> 💡 **Hinweis für GIMP 3.0:** GIMP erfordert oft, dass Plugins in einem Ordner abgelegt werden, der exakt denselben Namen wie das Skript trägt (z. B. ein Ordner namens `export_web`, der die Datei `export_web.py` enthält).

4. Starten Sie GIMP neu.

---

## 📖 Bedienung

Nach der erfolgreichen Installation finden Sie das Plugin direkt in der Menüleiste von GIMP:

Gehen Sie zu: **Datei** > **Exportieren** > **Export to web**

Der Prozess läuft im Hintergrund ab (nicht-interaktiv), um Ihnen Zeit und Klicks zu sparen.

---

## ✍️ Autoren

* **Entwickler:** Sergio Maya López
* **Jahr:** 2026

---

## 📄 Lizenz

Dieses Projekt steht unter der GNU General Public License (GPLv3). Sie können es gerne nach Ihren Bedürfnissen modifizieren, verbreiten und anpassen.
