#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   GIMP - The GNU Image Manipulation Program
#   Copyright (C) 1995 Spencer Kimball and Peter Mattis
#
#   gimp-tutorial-plug-in.py
#   sample plug-in to illustrate the Python plug-in writing tutorial
#   Copyright (C) 2023 Jacob Boerema
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi
from gi.repository import GLib

class ExportWeb (Gimp.PlugIn):
    def do_query_procedures(self):
        return [ "plugin-export-to-web" ]

    def do_set_i18n (self, name):
        return False

    def do_create_procedure(self, name):
        # Using Gimp.RunMode.NONINTERACTIVE if you want it to run without popups
        procedure = Gimp.ImageProcedure.new(self, name,
                                            Gimp.PDBProcType.PLUGIN,
                                            self.run, None)
        procedure.set_image_types("*")
        procedure.set_menu_label("Export to web")
        procedure.add_menu_path('<Image>/File/Export') # Put it in File > Export

        procedure.set_documentation("Exports file optimized for web (< 2MB target)",
                                    "Plugin export to web",
                                    name)
        procedure.set_attribution("Maya López & Sergio", "Sergio", "2026")
        return procedure

    def run(self, procedure, run_mode, image, drawables, config, run_data):
        # GIMP 3.0 passes 'drawables' as a list/array
        
        # 1. Flatten Image
        flatten_proc = Gimp.get_pdb().lookup_procedure('gimp-image-flatten')
        flatten_conf = flatten_proc.create_config()
        flatten_conf.set_property('image', image)
        flatten_proc.run(flatten_conf)
        
        width = image.get_width()
        height = image.get_height()

        # 2. Scale if too large
        if height > 3000:
            new_height = 3000
            new_width = int((width * new_height) / height)

            scale_proc = Gimp.get_pdb().lookup_procedure('gimp-image-scale')
            scale_conf = scale_proc.create_config()
            scale_conf.set_property('image', image)
            scale_conf.set_property('new-width', new_width)
            scale_conf.set_property('new-height', new_height)
            scale_proc.run(scale_conf)

        # 3. Set Resolution
        res_proc = Gimp.get_pdb().lookup_procedure('gimp-image-set-resolution')
        res_conf = res_proc.create_config()
        res_conf.set_property('image', image)
        res_conf.set_property('xresolution', 72.0)
        res_conf.set_property('yresolution', 72.0)
        res_proc.run(res_conf)

        # 4. Prepare Export File (Convert string path to GFile)
        # Note: You need a destination. For this example, I'll save to Desktop/web_export.jpg
        export_path = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DESKTOP) + "/web_export.jpg"
        save_file = Gio.File.new_for_path(export_path)

        # 5. JPEG Export
        export_proc = Gimp.get_pdb().lookup_procedure('file-jpeg-export')
        save_conf = export_proc.create_config()
        
        save_conf.set_property('image', image)
        save_conf.set_property('file', save_file)
        save_conf.set_property('run-mode', Gimp.RunMode.NONINTERACTIVE)
        save_conf.set_property('quality', 80) # 80% quality
        save_conf.set_property('optimize', True)
        save_conf.set_property('progressive', True)
        save_conf.set_property('sub-sampling', 0) # 0 is 4:4:4
        
        result = export_proc.run(save_conf)

        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())

# Important: Add Gio import at the top for the file handling
from gi.repository import Gio

Gimp.main(ExportWeb.__gtype__, sys.argv)