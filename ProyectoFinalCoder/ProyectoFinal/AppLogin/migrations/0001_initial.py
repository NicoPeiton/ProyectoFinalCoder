# Generated by Django 3.2.9 on 2021-12-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=10)),
                ('contraseña', models.CharField(max_length=10)),
            ],
        ),
    ]
