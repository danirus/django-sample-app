#-*- coding: utf-8 -*-

from django.db import models
from django.db.models import permalink
from django.utils.timezone import now
from django.utils.translation import ugettext, ugettext_lazy as _


class DiaryDay(models.Model):
    pub_date = models.DateField(unique=True, default=now)

    class Meta:
        verbose_name = _("diary day entry")
        verbose_name_plural = _("diary day entries")
        ordering = ("-pub_date",)
        get_latest_by = "pub_date"

    def __unicode__(self):
        return self.pub_date.isoformat()

    @permalink
    def get_absolute_url(self):
        return ("diaryday", None, {
                "year": self.pub_date.year,
                "month": self.pub_date.strftime("%b").lower(),
                "day": self.pub_date.day
        })


class DiaryDayEntry(models.Model):
    """A day in the dairy can have multiple entries per day"""
    diaryday = models.ForeignKey(DiaryDay, related_name="entries")
    body = models.TextField()

    class Meta:
        verbose_name = _("day entry")
        verbose_name_plural = _("day entries")
        ordering = ("id",)

    def __unicode__(self):
        return self.diaryday.pub_date.strftime(
            ugettext("Diary entry on %A, %d %B %Y at %H:%Mh"))

    def get_absolute_url(self):
        return self.diaryday.get_absolute_url()
