# Generated by Django 5.0.4 on 2024-05-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_company_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
