# Generated by Django 4.2.4 on 2023-09-19 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipos', '0003_grupo'),
        ('campeonato', '0004_remove_dirigentes_campeonato_asociado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuentro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.CharField(max_length=5, verbose_name='Hora Inicio')),
                ('hora_fin', models.CharField(max_length=5, verbose_name='Hora Fin')),
                ('fase', models.CharField(max_length=15)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campeonato.campeonato', verbose_name='Campeonato')),
                ('equipo_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Local', to='equipos.equipo', verbose_name='Local')),
                ('equipo_visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Visitante', to='equipos.equipo', verbose_name='Visitante')),
            ],
        ),
        migrations.CreateModel(
            name='Sanciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha Inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha Fin')),
                ('descripcion', models.CharField(max_length=100)),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipos.equipo')),
                ('jugador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipos.jugadores')),
            ],
        ),
        migrations.CreateModel(
            name='resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empate', models.BooleanField(default=False)),
                ('encuentro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuentros_equipos.encuentro')),
                ('ganador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ganador', to='equipos.equipo', verbose_name='Ganador')),
                ('perdedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Perdedor', to='equipos.equipo', verbose_name='Perdedor')),
            ],
        ),
    ]
