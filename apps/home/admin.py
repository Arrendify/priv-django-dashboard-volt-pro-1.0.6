# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 -Jonatan Sepulveda
"""

from django.contrib import admin
from .models import Rol,Profile, p_moral

class RolesAdmin(admin.ModelAdmin):
      readonly_fields=('id','created','updated')
admin.site.register(Rol,RolesAdmin)

admin.site.register(Profile)

admin.site.register(p_moral)

# Register your models here.
