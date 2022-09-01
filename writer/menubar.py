# Copyright 2022 Variscite LTD
# SPDX-License-Identifier: BSD-3-Clause

"""
Menu bar file.
"""

import os
import sys

import gi
gi.require_versions({'GdkPixbuf': "2.0", 'Gtk': "3.0"})
from gi.repository import GdkPixbuf, Gtk

from ._information import AUTHORS
from ._information import COMMENTS
from ._information import COPYRIGHT
from ._information import PROGRAM_NAME
from ._information import VERSION
from ._information import WEBSITE
from ._information import WEBSITE_LABEL
from ._information import LICENSE


class MenuBar(Gtk.MenuBar):
    def __init__(self, parent):
        super().__init__()
        item_about = Gtk.MenuItem.new_with_label('About')
        item_about.connect('activate', self.on_about, parent)

        menu_help = Gtk.Menu.new()
        menu_help.append(item_about)

        item_help = Gtk.MenuItem.new_with_label('Help')
        item_help.set_submenu(menu_help)

        self.new()
        self.append(item_help)

    def on_about(self, menu, parent):
        dialog = Gtk.AboutDialog(parent=parent)
        logo = GdkPixbuf.Pixbuf.new_from_file(
                  os.path.join(os.path.dirname(
                  os.path.realpath(__file__)), "assets", "variscite.png"))
        if logo != None:
            dialog.set_logo(logo)
        else:
            sys.write.stdout("A GdkPixbuf Error has occurred.\n")
        dialog.set_authors(AUTHORS)
        dialog.set_comments(COMMENTS)
        dialog.set_copyright(COPYRIGHT)
        dialog.set_license(LICENSE)
        dialog.set_program_name(PROGRAM_NAME)
        dialog.set_version(VERSION)
        dialog.set_website(WEBSITE)
        dialog.set_website_label(WEBSITE_LABEL)
        dialog.connect("response", self.on_about_dialog_button_clicked)
        dialog.run()

    def on_about_dialog_button_clicked(self, dialog, response):
        dialog.destroy()