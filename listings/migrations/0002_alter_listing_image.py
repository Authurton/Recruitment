# Generated by Django 5.0.4 on 2024-05-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%m/&d'),
        ),
    ]
