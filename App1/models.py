from django.db import models
from django.contrib.auth.models import User


class Ingredientes(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    
class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoria


class Cocktail(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingredientes)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    

class Comentarios(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    
    def __str__(self):
        return f'Comentario de {self.autor} en el coctél {self.cocktail}'
    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    
