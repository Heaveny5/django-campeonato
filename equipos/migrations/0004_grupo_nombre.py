# Generated by Django 4.2.4 on 2023-09-23 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0003_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='nombre',
            field=models.CharField(default='-', max_length=1, verbose_name='Grupo'),
        ),
    ]