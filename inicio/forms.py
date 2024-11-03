from django import forms

class BaseFormularioUsuario(forms.Form):
    cliente = forms.CharField(max_length=50)
    email = forms.CharField(max_length=35)
    direccion = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    intereses = forms.CharField(max_length=200)

class RegisterFormulario(BaseFormularioUsuario):...
    
class EditarUsuario(BaseFormularioUsuario):...

class BuscarCliente(forms.Form):
    
    cliente = forms.CharField(max_length=50, required=False)