# Generated by Django 2.2.5 on 2019-10-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_price',
            field=models.CharField(max_length=20),
        ),
    ]
