# Generated by Django 2.2.5 on 2019-11-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20191104_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rv_design',
        ),
        migrations.AlterField(
            model_name='review',
            name='rv_tatt',
            field=models.CharField(max_length=100),
        ),
    ]
