# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('raghuteja-ubuntu')

import logging
logger = logging.getLogger('raghuteja_ubuntu')

from raghuteja_ubuntu_lib.AboutDialog import AboutDialog

# See raghuteja_ubuntu_lib.AboutDialog.py for more details about how this class works.
class AboutRaghutejaUbuntuDialog(AboutDialog):
    __gtype_name__ = "AboutRaghutejaUbuntuDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutRaghutejaUbuntuDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

