# Generated by Django 3.0.3 on 2020-02-20 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Cuidad',
                'verbose_name_plural': 'Cuidades',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Epicentro',
            fields=[
                ('id_epicentro', models.AutoField(primary_key=True, serialize=False)),
                ('lalitud', models.CharField(max_length=45)),
                ('longitud', models.CharField(max_length=45)),
                ('profundidad', models.CharField(max_length=45)),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('valor_magnitud', models.CharField(max_length=45)),
                ('fk_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSismos.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('identificacion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Magnitud',
            fields=[
                ('id_tipo_magnitud', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Tipo de magnitud',
                'verbose_name_plural': 'Tipo de magnitudes',
            },
        ),
        migrations.CreateModel(
            name='Registro_Afectado',
            fields=[
                ('id_registro', models.AutoField(primary_key=True, serialize=False)),
                ('estado_persona', models.CharField(max_length=45)),
                ('fk_epicentro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSismos.Epicentro')),
                ('fk_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSismos.Persona')),
            ],
            options={
                'verbose_name': 'Registro de afectado',
                'verbose_name_plural': 'Registro de afectados',
            },
        ),
        migrations.AddField(
            model_name='epicentro',
            name='fk_tipo_magnitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSismos.Tipo_Magnitud'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='fk_departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionSismos.Departamento'),
        ),
    ]
