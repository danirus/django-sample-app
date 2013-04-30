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

from django.contrib import admin
from sample_app.models import DiaryDay, DiaryDayEntry


class DiaryDayEntryInline(admin.StackedInline):
    model = DiaryDayEntry
    extra = 0
        
class DiaryDayAdmin(admin.ModelAdmin):
    list_display = ("pub_date", "entries")
    inlines = [DiaryDayEntryInline,]
    
    def entries(self, obj):
        return obj.entries.count()

admin.site.register(DiaryDay, DiaryDayAdmin)
