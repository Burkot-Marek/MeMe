# Generated by Django 2.2 on 2019-05-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeRater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
