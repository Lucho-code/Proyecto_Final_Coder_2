from django.db import models
import uuid
from django.urls import reverse 

# Create your models here.


############################################################################### MODELO GENERO LITERARIO #####################################################################
class Genero(models.Model):
    name = models.CharField(max_length=50, help_text='Ingresa el género del libro')
    
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
    
    def __str__(self):
        return self.name

#################################################################################### MODELO LIBRO ###########################################################################
class Libro(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Autor', on_delete=models.SET_NULL, blank=True, null=True) #Clave externa utilizada porque el libro solo puede tener un autor, pero los autores pueden tener varios libros
    gender = models.ManyToManyField(Genero, help_text='Selecione el género del libro')
    language = models.ForeignKey('Lenguaje', on_delete=models.SET_NULL, null=True)
    resume = models.TextField(max_length=1000, help_text='Ingresa un breve resumen de libro', blank=True, null=True)
    
    # is_active = models.BooleanField(default=True) ver en las vistas
    # image = models.ImageField(upload_to = 'catalogo', blank=True, null=True) ver en las vistas
    
    class Meta:
        ordering = ['title', 'author']
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        
    def display_gender(self):
        return ', '.join([genre.name for genre in self.gender.all()[:3]])
    
    display_gender.short_description = 'Genero'

    #Devuelve el URL a una instancia particular de Libro ----> acordarse de gerenar url, vista y template detalle_libro
    #def get_absolute_url(self):
        #return reverse('book-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title

#################################################################################### MODELO AUTOR ###########################################################################
class Autor(models.Model):
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'firs_name']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def get_absolute_url(self):
        return reverse('datos_autor', args=[(self.id)])
    
    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.firs_name)

################################################################################## MODELO LENGUAJE ##########################################################################
class Lenguaje(models.Model):
    name = models.CharField(max_length=50, help_text='Ingresa el lenguaje del libro')
    
    def __str__(self):
        return self.name

################################################################################## MODELO ADMINISTRATIO ############################################################################################################################
class Administrativo(models.Model):
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    
################################################################################## MODELO USUARIO #########################################################################
class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    
