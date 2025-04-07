from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    paginas = models.IntegerField()
    autor = models.CharField(max_length=50)

    def __str__(self):
            return self.titulo