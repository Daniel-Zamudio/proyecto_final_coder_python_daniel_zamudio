from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    articulo = models.CharField(max_length=50)
    texto = RichTextField()
    autor = models.CharField(max_length=50)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="blogimagen", null=True, blank=True)
    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.fecha}"
    
class Img(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imgs", null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
