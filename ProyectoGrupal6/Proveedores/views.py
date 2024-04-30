# debemos import render de django shortcuts
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group

# debemos importar desde forms la clase creada con antelacion ProveedoresForm
from .forms import ProveedoresForm, RegistroUsuariosForm
from .models import Proveedores


# funcion personalizado para rutas restringidas
def login_required_message(function):
    def message(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied("Lo sentimos, no tienes permiso para acceder a esta página.")

    return message


# debemos crear una metodo para guardar el formulario con la informacion que proviene de forms
@login_required_message
def crear_proveedores(request):
    # verificar que el metodo utilizado por el formulario es POST
    if request.method == 'POST':
        # genero una variable donde le asigno toda la data proveniente de el formulario ProveedoresForm
        form = ProveedoresForm(request.POST)
        # verifico si la informacion del formulario es valida con la funcion is_valid()
        if form.is_valid():
            # si esto la informacion es valida procedo a guardar la informacion en la base de datos de django
            form.save()
            # en caso de exito, redirigimos a la pagina principal donde se visualizaran todos los proveedores
            return redirect('pagina_principal')
    else:
        # si la peticion enviada no es de tipo POST se devuelve un formulario vacio
        form = ProveedoresForm()

    # est retorno pemmitira al usuario ver el formulario y poder completarlo en el archivo form proveedores
    return render(request, 'form_proveedores.html', {'form': form})


# obtener el detalle de proveedores registrados de la base de datos
def proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'pagina_principal.html', {'proveedores': proveedores})


# funcion para acceder a la pagina si estamos registrados
def user_login(request):
    # preguntamos si el metodo de envio de la informacion es por post
    if request.method == 'POST':
        # si es asi obtener la informacion del formulario de username y password
        username = request.POST['username']
        password = request.POST['password']

        # ahora debemos autentificar al usuario con el metodo aunthenticate y almacenamos el resultado en user
        user = authenticate(request, username=username, password=password)

        # si la autentificacion es exitosa iniciamos sesion del usuario
        if user is not None:
            login(request, user)
            return redirect('userlogged')
        else:
            # si no es valido, volvemos al formulario de login
            return render(request, 'login.html', {'error': 'Usuario o contraseña inválidos'})
    else:
        # Si no es una petición POST, mostramos el formulario de login
        return render(request, 'login.html')


# cerrar sesion
def user_logout(request):
    # cerrar sesion
    logout(request)
    return redirect('login')


# vista posterior al login, con restriccion de acceso
@login_required_message
def user_logged(request):
    return render(request, 'user_logged.html')


# registrar usuario
def registrarse(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            user.groups.add(group)
            return redirect('login')
    else:
        form = RegistroUsuariosForm()
    return render(request, 'registrarse.html', {'form': form})
