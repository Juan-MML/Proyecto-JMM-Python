from django import forms

class RegisterFormulario(forms.Form):
    
    cliente = forms.CharField(max_length=50)
    email = forms.CharField(max_length=35)
    direccion = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    intereses = forms.CharField(max_length=200)

class BuscarCliente(forms.Form):
    
    cliente = forms.CharField(max_length=50, required=False)