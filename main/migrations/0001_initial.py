# Generated by Django 4.0.5 on 2022-06-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='null', upload_to='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
