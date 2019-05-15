from django.db import models

# Create your models here.


class Meme(models.Model):
    title = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='memes', unique=True)
    dateOfBirth = models.DateField()
    dateOfDeath = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=254)

    def __str__(self):
        return f'{self.title}'