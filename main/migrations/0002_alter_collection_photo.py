# Generated by Django 4.0.5 on 2022-06-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='photo',
            field=models.ImageField(upload_to='image'),
        ),
    ]
