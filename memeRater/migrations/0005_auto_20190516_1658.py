# Generated by Django 2.2 on 2019-05-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeRater', '0004_auto_20190516_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meme',
            name='title',
            field=models.CharField(max_length=62, unique=True),
        ),
    ]
