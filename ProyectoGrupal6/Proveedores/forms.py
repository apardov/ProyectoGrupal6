# se debe importar forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

# se debe importar el modelo creado anterirormente
from .models import Proveedores


class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['rut_proveedor', 'nombre_proveedor', 'nombre_representante', 'telefono', 'comuna', 'direccion']

class RegistroUsuariosForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required= True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'group' , 'password1', 'password2']
