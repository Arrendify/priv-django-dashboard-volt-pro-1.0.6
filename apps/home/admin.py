# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 -Jonatan Sepulveda
"""

from django.contrib import admin
from .models import Rol,Profile, form_test, p_moral, form_test

class RolesAdmin(admin.ModelAdmin):
      readonly_fields=('id','created','updated')
      
admin.site.register(Rol,RolesAdmin)

admin.site.register(Profile)

admin.site.register(p_moral)

admin.site.register(form_test)
# Register your models here.
