# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),    
    path('registropmoral', views.cpm_form, name='createm'),
    path('registropfisica', views.cpf_form, name='createf'),  #SUPUESTAMENTE ESTE PATH CONECTA LA VISTA MANDA LOS DATOS SI GUARDA EL OBJETO 
    path('listarpersonam', views.listarPersonam, name='listarPersonam'),  #SUPUESTAMENTE ESTE PATH CONECTA LA VISTA MANDA LOS DATOS SI GUARDA EL OBJETO 
    path('listarpersonaf', views.listarPersonaf, name='listarPersonaf'),  #SUPUESTAMENTE ESTE PATH CONECTA LA VISTA MANDA LOS DATOS SI GUARDA EL OBJETO 
    path('editarpf/<id>', views.editarpf, name='editarpf'),
    path('editarpm/<id>', views.editarpm, name='editarpm'),
    path('test', views.testform, name='test'),  #SUPUESTAMENTE ESTE PATH CONECTA LA VISTA MANDA LOS DATOS SI GUARDA EL OBJETO 
    path('removerpm/<id>', views.removerpm, name='removerpm'),
    path('removerpf/<id>', views.removerpf, name='removerpf'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
