# Generated by Django 4.1.3 on 2022-11-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingcentermodel',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parkingcentermodel',
            name='img',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]