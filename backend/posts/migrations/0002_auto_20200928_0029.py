# Generated by Django 3.1.1 on 2020-09-28 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, to='categories.Category'),
        ),
    ]
