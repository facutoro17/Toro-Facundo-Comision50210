from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("login/", iniciarSesion, name="Login"),
    path("registro/", registrar, name="Registrar"),
    path("logout/", cerrarSesion, name="Logout"),
    path("editarUsuario/", editarUsuario, name= "EditarUsuario"),
    path("agregarAvatar/", agregarAvatar, name="Avatar"),
    


    #CRUD Ingredientes
    path("ingredientes/ver", listaIngredientes.as_view(template_name="App1/ingredientes/ingredientes_list.html"), name= "listaIngredientes"),
    path("ingredientes/<int:pk>", detalleIngredientes.as_view(template_name="App1/ingredientes/ingredientes_detail.html"), name= "detalleIngredientes"),
    path("ingredientes/crear/<int:pk>", crearIngredientes.as_view(template_name="App1/ingredientes/ingredientes_form.html"), name= "crearIngrediente"),
    path("ingredientes/editar/<int:pk>", editarIngredientes.as_view(template_name="App1/ingredientes/ingredientes_form.html"), name= "editarIngredientes"),
    path("ingredientes/eliminar/<int:pk>", eliminarIngredientes.as_view(template_name="App1/ingredientes/ingredientes_confirm.html"), name= "eliminarIngredientes"),


    #CRUD Categoria
    path("categoria/ver", listaCategoria.as_view(), name= "listaCategoria"),
    path("categoria/<int:pk>", detalleCategoria.as_view(), name= "detalleCategoria"),
    path("categoria/crear/<int:pk>", crearCategoria.as_view(), name= "crearCategoria"),
    path("categoria/editar/<int:pk>", editarCategoria.as_view(), name= "editarCategoria"),
    path("categoria/eliminar/<int:pk>", eliminarCategoria.as_view(), name= "eliminarCategoria"),


    #CRUD Cocktail
    path("cocktail/ver", listaCocktail.as_view(), name= "listaCocteles"),
    path("cocktail/<int:pk>", detalleCocktail.as_view(), name= "detalleCocteles"),
    path("cocktail/crear/<int:pk>", crearCocktail.as_view(), name= "crearCocteles"),
    path("cocktail/editar/<int:pk>", editarCocktail.as_view(), name= "editarCocteles"),
    path("cocktail/eliminar/<int:pk>", eliminarCocktail.as_view(), name= "eliminarCocteles"),


    #CRUD Comentarios
    path("comentario/ver", listaComentarios.as_view(), name= "listaComentarios"),
    path("comentario/<int:pk>", detalleComentarios.as_view(), name= "detalleComentarios"),
    path("comentario/crear/<int:pk>", crearComentarios.as_view(), name= "crearComentarios"),
    path("comentario/editar/<int:pk>", editarComentarios.as_view(), name= "editarComentarios"),
    path("comentario/eliminar/<int:pk>", eliminarComentarios.as_view(), name= "eliminarComentarios"),



]