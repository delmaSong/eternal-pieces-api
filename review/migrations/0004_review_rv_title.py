# Generated by Django 2.2.5 on 2019-11-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20191103_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rv_title',
            field=models.CharField(default='title', max_length=50),
            preserve_default=False,
        ),
    ]
