from django.db import models

# Create your models here.
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=2000)
    image = models.ImageField(upload_to= 'images')
    song = models.FileField(upload_to= 'songs')
    movie = models.CharField(max_length=2000, default="")


    def __str__(self):
        return self.name

