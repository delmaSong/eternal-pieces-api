# Generated by Django 2.2.5 on 2019-09-25 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join_tattist',
            name='tatt_profile',
            field=models.ImageField(upload_to=''),
        ),
    ]
