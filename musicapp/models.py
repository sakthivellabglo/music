from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
LANGUAGE_CHOICES = (
        ("t", "tamil"),
        ("e", "english"),
        ("h","hindi"),
        ('m','malayalam')
    )

class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    image = models.ImageField(upload_to="images")
    age = models.PositiveSmallIntegerField()


class Artist(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="images")
    DOB = models.DateField()
    language = models.CharField(max_length=1,choices=LANGUAGE_CHOICES)
    def __str__(self):
        return self.name

class Songs(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to="images",blank=True)
    song = models.FileField(upload_to="audio")
    language = models.CharField(max_length=1,choices=LANGUAGE_CHOICES)
    artist = models .ForeignKey(Artist,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Playlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=40,blank=False,null= False)
    song = models.ManyToManyField(Songs)
    def __str__(self):
        return self.playlist_name

class Favourite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(Songs,on_delete=models.CASCADE)

class Resent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(Songs,on_delete=models.CASCADE)

# Create your models here.
