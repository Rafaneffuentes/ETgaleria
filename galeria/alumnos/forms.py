#CREAR CLASES PARA FORMULARIOS
from django.forms import ModelForm
from django import forms
from .models import  TiposObras, Obras

class ObrasForm(forms.ModelForm):
    class Meta:
        model = Obras 
        #fields = ['codigo', 'nombre', 'sence', 'idArea', 
         #         'modalidad', 'objetivo', 'horas', 'img'] 
   
        fields = '__all__' 


