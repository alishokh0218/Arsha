from django.contrib import admin

# Register your models here.
from appfolder.models import *


class AdminWeb(admin.ModelAdmin):
    list_display = ['id', 'nomi']

    def __str__(self):
        return self.nomi


admin.site.register(Web, AdminWeb)


class AdminServis(admin.ModelAdmin):
    list_display = ['id', 'ism', 'malumot', 'rasm', 'sana']


admin.site.register(Servis, AdminServis)


class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id', 'ism', 'web', 'sana', 'rasm']


admin.site.register(Portfolio, AdminPortfolio)


class AdminTeam(admin.ModelAdmin):
    list_display = ['id', 'ism', 'lavozimi', 'malumot', 'insta', 'tg', 'twit', 'facebook', 'rasm', 'sana']


admin.site.register(Team, AdminTeam)

class AdminContact(admin.ModelAdmin):
    list_display = ['id','ism','yonalish','malumot','email']

admin.site.register(Contact, AdminContact)
