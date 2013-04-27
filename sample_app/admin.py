#-*- coding: utf-8 -*-

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
