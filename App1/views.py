from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#Vista de inicio
def inicio(request):
    return render(request, "App1/inicio.html", {"titulo":"Bienvenido a tu página favorita de cocteles"})


#Vista de inicio de sesión
def iniciarSesion(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user:
                login(request, user)
                
                return render(request, "App1/inicio.html", {"titulo":f"Bienvenidx {user.username}"})
        
        else: 
            return render(request, "App1/inicio.html", {"titulo":"Datos incorrectos."})
    
    else:
        form = AuthenticationForm()

    return render(request, "App1/login.html", {"formulario":form, "titulo":"Aqui puedes iniciar sesión!"})


##Vista de cerrar sesión
def cerrarSesion(request):
    
    logout(request)

    return render(request, "App1/inicio.html", {"titulo":"Ha cerrado sesión correctamente."})


#Vista de registrar usuario
def registrar(request):

    if request.method == "POST":
        form = RegistroUsuario(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "App1/inicio.html", {"titulo":"Usuario creado."})
        
    else:
        form = RegistroUsuario()

    return render(request, "App1/registro.html", {"formulario":form, "titulo":"Registra tu usuario"})


#Vista de editar usuario
@login_required
def editarUsuario(request):

    usuario = request.user
    form = FormularioEditar(initial={
                "email":usuario.email,
                "first_name":usuario.first_name,
                "last_name":usuario.last_name,
            })

    if request.method == "POST":
        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "App1/inicio.html", {"titulo":"Usuario editado con éxito"})
        
        else:

            form = FormularioEditar(initial={
                "email":usuario.email,
                "first_name":usuario.first_name,
                "last_name":usuario.last_name,
            })
        
        return render(request, "App1/editarPerfil.html", {"formulario":form, "usuario":usuario, "titulo":"Edita tu usuario."})

    return render(request, "App1/editarPerfil.html", {"formulario":form, "titulo":"Edita tu usuario."})

#Vista de agregar avatar
@login_required
def agregarAvatar(request):

    if request.method == "POST":
        form = FormularioAvatar(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "App1/inicio.html", {"titulo":"Avatar agregado correctamente."})
        
    else:

        form = FormularioAvatar()
    
    return render (request, "App1/agregarAvatar.html", {"formulario":form, "titulo":"Agrega tu avatar"})



#CRUD Ingredientes

class listaIngredientes(ListView):

    model = Ingredientes
    urls_name = "listaIngredientes"

class detalleIngredientes(LoginRequiredMixin, DetailView):

    model = Ingredientes

class crearIngredientes(LoginRequiredMixin, CreateView):

    model = Ingredientes
    success_url = "/App1/"
    fields = ["nombre"]

class editarIngredientes(LoginRequiredMixin, UpdateView):

    model = Ingredientes
    success_url = "/App1/"
    fields = ["nombre"]

class eliminarIngredientes(LoginRequiredMixin, DeleteView):

    model = Ingredientes
    success_url = "/App1/"


#CRUD Categoria

class listaCategoria(ListView):

    model = Categoria

class detalleCategoria(LoginRequiredMixin, DetailView):

    model = Categoria

class crearCategoria(LoginRequiredMixin, CreateView):

    model = Categoria
    success_url = "/App1/"
    fields = ["categoria"]

class editarCategoria(LoginRequiredMixin, UpdateView):

    model = Categoria
    success_url = "/App1/"
    fields = ["categoria"]

class eliminarCategoria(LoginRequiredMixin, DeleteView):

    model = Categoria
    success_url = "/App1/"

#CRUD Cocktail

class listaCocktail(ListView):

    model = Cocktail

class detalleCocktail(LoginRequiredMixin, DetailView):

    model = Cocktail

class crearCocktail(LoginRequiredMixin, CreateView):

    model = Cocktail
    success_url = "/App1/"
    fields = ["nombre", "autor", "categoria", "ingredientes", "descripcion"]

class editarCocktail(LoginRequiredMixin, UpdateView):

    model = Cocktail
    success_url = "/App1/"
    fields = ["nombre", "autor", "categoria", "ingredientes", "descripcion"]

class eliminarCocktail(LoginRequiredMixin, DeleteView):

    model = Cocktail
    success_url = "/App1/"

#CRUD Comentarios

class listaComentarios(ListView):

    model = Comentarios

class detalleComentarios(LoginRequiredMixin, DetailView):

    model = Comentarios

class crearComentarios(LoginRequiredMixin, CreateView):

    model = Comentarios
    success_url = "/App1/"
    fields = ["cocktail", "autor", "texto"]

class editarComentarios(LoginRequiredMixin, UpdateView):

    model = Comentarios
    success_url = "/App1/"
    fields = ["cocktail", "autor", "texto"]

class eliminarComentarios(LoginRequiredMixin, DeleteView):

    model = Comentarios
    success_url = "/App1/"