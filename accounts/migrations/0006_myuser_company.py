# Generated by Django 5.0.4 on 2024-05-15 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_cvview_created_at'),
        ('listings', '0002_company_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='listings.company'),
        ),
    ]
