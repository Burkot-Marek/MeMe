# Generated by Django 2.2 on 2019-05-17 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memeRater', '0010_auto_20190517_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='additional',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='memeRater.MemeAdditional'),
        ),
    ]
