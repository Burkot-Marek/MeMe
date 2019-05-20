from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class MemeGroup(models.Model):
    memeGroup = models.CharField(max_length=30, default="")

    def __str__(self):
        return f'{self.memeGroup}'


class Meme(models.Model):
    title = models.CharField(max_length=62, unique=True)
    picture = models.ImageField(upload_to='memes', unique=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    dateOfDeath = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=254)
    public = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    adminClass = models.ForeignKey(MemeGroup, on_delete=models.CASCADE)
                                                                                                                        #dodać podklasę połączoną połaczeniem 1 do 1 zawierającą klase mema i skalę mema

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    comment = models.CharField(default="", blank=True, max_length=30)
    dankScale = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.meme}:  {self.comment}'
