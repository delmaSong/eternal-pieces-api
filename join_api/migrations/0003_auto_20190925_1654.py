# Generated by Django 2.2.5 on 2019-09-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_api', '0002_auto_20190925_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join_tattist',
            name='tatt_profile',
            field=models.ImageField(upload_to='profiles'),
        ),
    ]