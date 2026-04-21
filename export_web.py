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
        return [ "-plugin-export-to-web" ]

    def do_set_i18n (self, name):
        return False

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(self, name,
                                            Gimp.PDBProcType.PLUGIN,
                                            self.run, None)

        procedure.set_image_types("*")

        procedure.set_menu_label("Export to web")
        procedure.add_menu_path('<Image>/Export to web')

        procedure.set_documentation("This plugin export files which size is less than 2 MB",
                                    "Plugin export to web",
                                    name)
        procedure.set_attribution("Maya López", "Sergio", "2026")

        return procedure

    def run(self, procedure, run_mode, image, drawable, config, run_data, filename):
        #name_image = image.name
        
        procedure = Gimp.get_pdb().lookup_procedure('gimp-image-flatten');
        config = procedure.create_config();
        config.set_property('image', image);
        result = procedure.run(config);
        success = result.index(0);
        layer = result.index(1)
        
        width = image.width
        height = image.height

        if height < 3000:
            new_height = 3000
            new_width = (width * new_height)/ height

            procedure = Gimp.get_pdb().lookup_procedure('gimp-image-resize'); 
            config = procedure.create_config(); 
            config.set_property('image', image); 
            config.set_property('new-width', new_width); 
            config.set_property('new-height', new_height); 
            config.set_property('offx', 0); 
            config.set_property('offy', 0); 
            result = procedure.run(config); 
            success = result.index(0)

            procedure = Gimp.get_pdb().lookup_procedure('gimp-image-set-resolution'); 
            config = procedure.create_config(); 
            config.set_property('image', image); 
            config.set_property('xresolution', 72); 
            config.set_property('yresolution', 72);
            result = procedure.run(config);
            success = result.index(0)

        else :
            print("The file is to small")
        

        procedure = Gimp.get_pdb().lookup_procedure('file-jpeg-export'); 
        config = procedure.create_config(); 
        config.set_property('run-mode', Gimp.RunMode.INTERACTIVE); 
        config.set_property('image', image); 
        config.set_property('file', filename); 
        #config.set_property('options', options); 
        config.set_property('quality', 0.8); 
        config.set_property('smoothing', 0.0000); 
        config.set_property('optimize', True); 
        config.set_property('progressive', True); 
        config.set_property('cmyk', False); 
        config.set_property('sub-sampling', "sub-sampling-1x1: 4:4:4"); 
        config.set_property('baseline', True); 
        config.set_property('restart', 0); 
        config.set_property('dct', "integer"); 
        config.set_property('include-exif', False); 
        config.set_property('include-iptc', True); 
        config.set_property('include-xmp', False); 
        config.set_property('include-color-profile', False); 
        config.set_property('include-thumbnail', False); 
        config.set_property('include-comment', False); 
        result = procedure.run(config); success = result.index(0)

        procedure = Gimp.get_pdb().lookup_procedure('gimp-file-save'); 
        config = procedure.create_config(); 
        config.set_property('run-mode', Gimp.RunMode.INTERACTIVE); 
        config.set_property('image', image); 
        config.set_property('file', filename); 
        #config.set_property('options', options); 
        result = procedure.run(config); 
        success = result.index(0)



        # do what you want to do, then, in case of success, return:
        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())

Gimp.main(ExportWeb.__gtype__, sys.argv)
      