from django.db import models

# Create your models here.


class Meme(models.Model):
    title = models.CharField(max_length=62, unique=True)
    picture = models.ImageField(upload_to='memes', unique=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    dateOfDeath = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=254)
    public = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    memeClass = models.CharField(max_length=30, blank=True, null=True)
    #dankScale = models.
    #dodać podklasę połączoną połaczeniem 1 do 1 zawierającą klase mema i skalę mema

    def __str__(self):
        return f'{self.title}'