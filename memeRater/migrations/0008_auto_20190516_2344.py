# Generated by Django 2.2 on 2019-05-16 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeRater', '0007_auto_20190516_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='public',
            field=models.CharField(max_length=6),
        ),
    ]
