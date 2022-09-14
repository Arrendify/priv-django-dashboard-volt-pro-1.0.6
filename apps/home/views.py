# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from multiprocessing import context
from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from requests import get
from .models import p_fisica, p_moral, inmuebles
from django.shortcuts import redirect, render, get_object_or_404
from .forms import MoralForm, form_test, FisicaForm, InmueblesForm
from django.contrib.auth.models import User


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

#Modulo para persona moral
#Formulario de registro de persona moral
def cpm_form(request):
    if request.method == "POST":
        form = MoralForm(request.POST or None)
        print(request.POST)
        if form.is_valid():
            print("valido")
            formpm = form.save(commit=False)
            formpm.user = request.user
            print(formpm)
            formpm.save()
            return redirect('/listarpersonam')
        else:
            print(" No valido")
            print(form.errors)
            form= MoralForm()
    
    return render(request, 'home/registro-p-moral.html', {'form' : form})

#Formulario de registro de persona física
def cpf_form(request):
    if request.method == "POST":
        form = FisicaForm(request.POST or None)
        print(request.POST)
        if form.is_valid():
            print("valido")
            formpf = form.save(commit=False)
            formpf.user = request.user
            print(formpf)
            formpf.save()
            return redirect('/listarpersonaf')
        else:
            print(" No valido")
            print(form.errors)
            form= FisicaForm()
    
    return render(request, 'home/registro-p-fisica.html', {'form' : form})

#listar personas
def listarPersonam(request):
    personas=p_moral.objects.all().filter(user_id=request.user)
    print(personas)
    return render(request, 'home/tabla-personasm.html', {'personas': personas })

def listarPersonaf(request):
    personas=p_fisica.objects.all().filter(user_id=request.user)
    print(personas)
    return render(request, 'home/tabla-personasf.html', {'personas': personas })

#editar registros
def editarpf(request, id):
    # fetch the object related to passed id
    objpf = p_fisica.objects.get(id = id)
    form = FisicaForm(request.POST or None, instance=objpf)
    if form.is_valid():
        print("valido")
        formpf = form.save(commit=False)
        formpf.user = request.user
        formpf.save()
        return redirect('/listarpersonaf')      
          
    context={'objpf':objpf}
 
    return render(request, "home/editpf.html", context)

def editarpm(request, id):
    # fetch the object related to passed id
    objpm = p_moral.objects.get(id = id)
    form = MoralForm(request.POST or None, instance=objpm)
    if form.is_valid():
        formpm = form.save(commit=False)
        formpm.user = request.user
        formpm.save()
        return redirect('/listarpersonam')      
          
    context={'objpm':objpm}
 
    return render(request, "home/editpm.html", context)

#remover registros
def removerpm(request, id):
    objpm = p_moral.objects.get(id = id)
    objpm.delete()

    return HttpResponseRedirect(reverse('listarPersonam'))

def removerpf(request, id):
    objpf = p_fisica.objects.get(id = id)
    objpf.delete()

    return HttpResponseRedirect(reverse('listarPersonaf'))



#modulo inmuebles
def formInmueble(request):
    if request.method == 'POST':
        form=InmueblesForm(request.POST or None)
        print(request.POST)
        if form.is_valid():
            print("Valido")
            formin = form.save(commit=False)
            formin.user = request.user
            print(formin)
            formin.save()
            return redirect('/listarinmuebles')
        else:
            print("No valido")
            print(form.errors)
            form= InmueblesForm()

    return render(request, 'home/registro-inmueble.html', {'form': form})

def listarInmueble(request):
    objinmuebles=inmuebles.objects.all().filter(user_id=request.user)
    print(objinmuebles)
    return render(request, 'home/tabla-inmuebles.html', {'objinmuebles': objinmuebles })

def verInmueble(request, id):
    verinmueble=inmuebles.objects.get(id=id)
    print(verinmueble)
    return render(request, 'home/vista-inmueble.html', {'verinmueble': verinmueble })

def editarInmueble(request, id):
    objin = inmuebles.objects.get(id = id)
    form = InmueblesForm(request.POST or None, instance=objin)
    print(request.POST)
    if form.is_valid():
        print("valido")
        formin = form.save(commit=False)
        formin.user = request.user        
        formin.save()
        return redirect('/listarinmuebles')      
          
    context={'objin':objin}
 
    return render(request, "home/editin.html", context)

def removerInmueble(request, id):
    objin = inmuebles.objects.get(id = id)
    objin.delete()

    return HttpResponseRedirect(reverse('listarInmueble'))


#views pruebas
def testform(request):
    if request.method == "POST":
        print(request.POST)
        formp= form_test(request.POST or None)
        if formp.is_valid():
            print("valido")
            obj = formp.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('/listarpersonam')
            
        else:
            print("No valido")
            print(formp.errors)
            formp= form_test()

    context= {'formp' : formp}

    return render(request, 'home/registro-p-f.html', context)

# def editarPrueba(request, id):
#     # fetch the object related to passed id
#     objpm = p_moral.objects.get(id = id)
#     form = MoralForm(request.POST or None, instance=objpm)
#     if form.is_valid():
#         print("valido")
#         form.save()
#         return redirect('/listarpersonam')      
          
#     context={'objpm':objpm}
 
#     return render(request, "home/editpm.html", context)

def listarPrueba(request):
    personas=p_fisica.objects.all().filter(user_id=request.user)
    print(personas)
    return render(request, 'home/tabla-personasf.html', {'personas': personas })

# def removerprueba(request, id):
#     objpm = p_moral.objects.get(id = id)
#     objpm.delete()

#     return render(request, "home/tabla-personasm.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
