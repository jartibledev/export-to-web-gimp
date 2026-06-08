# [:es:](README_ES.md) [:de:](README_DE.md) [:fr:](README_FR.md) 
# Export to Web - GIMP 3.0 Plugin

Optimize your images for the web with a single click! **Export to Web** is a Python-based plugin developed for **GIMP 3.0** that automates the process of compressing, resizing, and preparing images to ensure they stay under 2MB and load fast on any website.

## 🚀 Features

The plugin automatically performs the following tasks on the active image:
1. **Flatten Image:** Combines all visible layers into a single background layer.
2. **Smart Resizing:** If the image height exceeds `3000px`, it scales it down proportionally to avoid excessively large files.
3. **Resolution Adjustment:** Changes the image resolution to `72 DPI` (the standard for web displays).
4. **Optimized Export (.jpg):** Saves the file in JPEG format at `80%` quality, using progressive encoding and 4:4:4 sub-sampling to maintain a perfect balance between file size and visual fidelity.

### 📁 File Destination:
* If the original image **has already been saved**, the plugin will generate the optimized `.jpg` file in the **same directory** with the same name.
* If it is a **new or untitled image**, it will be automatically exported to your **Desktop** under the name `web_export.jpg`.

---

## 🛠️ Requirements

* **GIMP 3.0** (or higher) with Python 3 Plugin support.
* GNOME Object Introspection system libraries (`PyGObject`, `Gio`, `Gimp 3.0`).

---

## 🔧 Installation

To install the plugin, follow these steps:

1. **Download or copy** the script file and name it (e.g., `export_web.py`).
2. Make the file **executable**.
   * *On Linux/macOS:* Open a terminal and run `chmod +x export_web.py`.
3. **Move the file** to your GIMP 3.0 plug-ins directory:
   * **Linux:** `~/.config/GIMP/3.0/plug-ins/`
   * **Windows:** `%APPDATA%\GIMP\3.0\plug-ins\`
   * **macOS:** `~/Library/Application Support/GIMP/3.0/plug-ins/`

> 💡 **Note for GIMP 3.0:** GIMP often requires plugins to be placed inside a folder with the exact same name as the script (e.g., a folder named `export_web` containing the `export_web.py` file).

4. Restart GIMP.

---

## 📖 How to Use

Once properly installed, you will find the plugin directly in the GIMP menu bar:

Go to: **File** > **Export** > **Export to web**

The process will run non-interactively (in the background) to save you time and clicks.

---

## ✍️ Authors

* **Developers:** Maya López & Sergio
* **Year:** 2026

---

## 📄 License

This project is licensed under the GNU General Public License (GPLv3). Feel free to modify, distribute, and adapt it to your needs.
