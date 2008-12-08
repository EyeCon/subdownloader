#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (C) 2007 Ivan Garcia capiscuas@gmail.com
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    see <http://www.gnu.org/licenses/>.

import re, os, logging
import modules.videofile as videofile
import modules.subtitlefile as subtitlefile
from FileManagement import get_extension, clear_string, without_extension
from languages import Languages, autodetect_lang

log = logging.getLogger("subdownloader.FileManagement.Video")

def isVideofile(filepath):
    if get_extension(filepath).lower() in videofile.VIDEOS_EXT:
        return True
    return False
