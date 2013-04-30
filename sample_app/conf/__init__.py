#-*- coding: utf-8 -*-

# django-sample-app - A Django app with setup, unittests, docs and demo
# Copyright (C) 2013,  Daniel Rus Morales

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings as django_settings
from django.utils.functional import LazyObject

from sample_app.conf import defaults as app_settings


class LazySettings(LazyObject):
    def _setup(self):
        self._wrapped = Settings(app_settings, django_settings)

def update_dict_in_depth(a, b):
    """Updates dict 'a' in depth with values of dict 'b' (not for sequences)"""
    for k, v in b.iteritems():
        if a.get(k, None) and type(v) == dict:
                update_dict_in_depth(a[k], v)
        else:
            a[k] = v

class Settings(object):
    def __init__(self, *args):
        for item in args:
            for attr in dir(item):
                if attr == attr.upper():
                    setattr(self, attr, getattr(item, attr))

    def __setattr__(self, name, value):
        obj_attr = getattr(self, name, None)
        if obj_attr and type(obj_attr) == dict:
            update_dict_in_depth(obj_attr, value)
        else:
            object.__setattr__(self, name, value)

settings = LazySettings()
