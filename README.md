# [:es:](README_ES.md) [:de:](README_DE.md) [:fr:](README_FR.md) 
# Export to Web - GIMP 3.0 Plugin

¡Optimiza tus imágenes para la web con un solo clic! **Export to Web** es un plugin desarrollado en Python para **GIMP 3.0** que automatiza el proceso de compresión, redimensionado y preparación de imágenes para que pesen menos de 2MB y carguen rápido en cualquier sitio web.

## 🚀 Características

El plugin realiza de forma automática las siguientes tareas sobre la imagen activa:
1. **Aplanado de imagen (`Flatten`):** Combina todas las capas visibles en una sola capa de fondo.
2. **Redimensionado inteligente:** Si la altura de la imagen supera los `3000px`, la escala proporcionalmente para evitar archivos excesivamente grandes.
3. **Ajuste de resolución:** Cambia la resolución a `72 DPI` (el estándar para pantallas web).
4. **Exportación optimizada (.jpg):** Salva el archivo en formato JPEG con una calidad del `80%`, codificación progresiva y sub-sampling 4:4:4 para mantener un balance perfecto entre peso y fidelidad visual.

### 📁 Destino del archivo:
* Si la imagen original **ya estaba guardada**, el plugin generará el archivo `.jpg` optimizado en la **misma carpeta** con el mismo nombre.
* Si es una imagen **nueva o sin título**, se exportará automáticamente en tu **Escritorio** bajo el nombre `web_export.jpg`.

---

## 🛠️ Requisitos

* **GIMP 3.0** (o superior) con soporte para Plugins de Python 3.
* Librerías del sistema de introspección de GNOME (`PyGObject`, `Gio`, `Gimp 3.0`).

---

## 🔧 Instalación

Para instalar el plugin, sigue estos pasos:

1. **Descarga o copia** el archivo del script y nómbralo (por ejemplo: `export_web.py`).
2. Dale **permisos de ejecución** al archivo. 
   * *En Linux/macOS:* Abre una terminal y ejecuta `chmod +x export_web.py`.
3. **Mueve el archivo** a tu directorio de plug-ins de GIMP 3.0:
   * **Linux:** `~/.config/GIMP/3.0/plug-ins/`
   * **Windows:** `%APPDATA%\GIMP\3.0\plug-ins\`
   * **macOS:** `~/Library/Application Support/GIMP/3.0/plug-ins/`

> 💡 **Nota para GIMP 3.0:** A veces, GIMP requiere que los plugins organizados en carpetas tengan el mismo nombre que el directorio (Ej: una carpeta llamada `export_web` y dentro el archivo `export_web.py`).

4. Reinicia GIMP.

---

## 📖 Modo de Uso

Una vez instalado correctamente, encontrarás el plugin directamente en la barra de menús de GIMP:

Vayan a: **Archivo** > **Exportar** > **Export to web**

El proceso se ejecutará de forma no interactiva (en segundo plano) para ahorrarte clics.

---

## ✍️ Autores

* **Desarrolladores:** Maya López & Sergio
* **Año:** 2026

---

## 📄 Licencia

Este proyecto está bajo la Licencia Pública General GNU (GPLv3). Siéntete libre de modificarlo, distribuirlo y adaptarlo a tus necesidades.
