# Generated by Django 2.2.2 on 2019-07-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
