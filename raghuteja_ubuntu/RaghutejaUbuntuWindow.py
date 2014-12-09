# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('raghuteja-ubuntu')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('raghuteja_ubuntu')

from raghuteja_ubuntu_lib import Window
from raghuteja_ubuntu.AboutRaghutejaUbuntuDialog import AboutRaghutejaUbuntuDialog
from raghuteja_ubuntu.PreferencesRaghutejaUbuntuDialog import PreferencesRaghutejaUbuntuDialog

# See raghuteja_ubuntu_lib.Window.py for more details about how this class works
class RaghutejaUbuntuWindow(Window):
    __gtype_name__ = "RaghutejaUbuntuWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(RaghutejaUbuntuWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutRaghutejaUbuntuDialog
        self.PreferencesDialog = PreferencesRaghutejaUbuntuDialog

        # Code for other initialization actions should be added here.

