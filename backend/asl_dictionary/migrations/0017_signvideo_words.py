# Generated by Django 3.0.5 on 2020-04-30 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asl_dictionary', '0016_auto_20200424_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='signvideo',
            name='words',
            field=models.ManyToManyField(blank=True, to='asl_dictionary.SignWord'),
        ),
    ]