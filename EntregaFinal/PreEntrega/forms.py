from django import forms
from .models import ProductosH, ProductosM, ProductosN

class CrearProductosH(forms.ModelForm):

    class Meta:
        model = ProductosH
        fields = '__all__'

class CrearProductosM(forms.ModelForm):
    
    class Meta:
        model = ProductosM
        fields = '__all__'

class CrearProductosN(forms.ModelForm):
    
    class Meta:
        model = ProductosN
        fields = '__all__'