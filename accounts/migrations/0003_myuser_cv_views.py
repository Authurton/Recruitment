# Generated by Django 5.0.4 on 2024-05-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myuser_pro_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='cv_views',
            field=models.BooleanField(default=False),
        ),
    ]
