from django.db import models

class Banda(models.Model):
    nome = models.CharField('Banda',max_length = 150)

    def __str__(self):
        
        return self.nome

    class Meta:
        verbose_name = 'Banda'
        verbose_name_plural = 'Bandas'
        ordering = ['nome']

class Albun(models.Model):
    titulo = models.CharField('Album',max_length = 150)
    banda = models.ForeignKey(Banda, on_delete=models.PROTECT)
    data = models.DateTimeField('Data')

    def __str__(self):
        
        return self.titulo


    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'
        ordering = ['titulo']
    
class Musica(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    segundos = models.IntegerField('Segundos')
    album = models.ForeignKey(Albun, on_delete=models.PROTECT)
    
    def __str__(self):
        
        return self.titulo
    
    
    class Meta:
        verbose_name = 'Musica'
        verbose_name_plural = 'Musicas'
        ordering = ['id']