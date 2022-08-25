from django import forms
from .models import  p_fisica, p_moral, form_test

class MoralForm(forms.ModelForm):
    class Meta:
        model=p_moral
        fields= '__all__'

class FisicaForm(forms.ModelForm):
    class Meta:
        model=p_fisica
        fields='__all__'        

class form_test(forms.ModelForm):
    class Meta:
        model=form_test
        fields='__all__'

# class InmueblesForm(forms.ModelForm):
    
#     class Meta:
#         model = inmuebles
#         fields = '__all__'
