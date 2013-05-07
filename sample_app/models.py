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

from django.db import models
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext, ugettext_lazy as _


@python_2_unicode_compatible
class DiaryDay(models.Model):
    pub_date = models.DateField(unique=True, default=now)

    class Meta:
        verbose_name = _("diary day entry")
        verbose_name_plural = _("diary day entries")
        ordering = ("-pub_date",)
        get_latest_by = "pub_date"

    def __str__(self):
        return self.pub_date.isoformat()

    @permalink
    def get_absolute_url(self):
        return ("diaryday", None, {
                "year": self.pub_date.year,
                "month": self.pub_date.strftime("%b").lower(),
                "day": self.pub_date.day
        })


@python_2_unicode_compatible
class DiaryDayEntry(models.Model):
    """A day in the dairy can have multiple entries per day"""
    diaryday = models.ForeignKey(DiaryDay, related_name="entries")
    body = models.TextField()

    class Meta:
        verbose_name = _("day entry")
        verbose_name_plural = _("day entries")
        ordering = ("id",)

    def __str__(self):
        return self.diaryday.pub_date.strftime(
            ugettext("Diary entry on %A, %d %B %Y at %H:%Mh"))

    def get_absolute_url(self):
        return self.diaryday.get_absolute_url()
