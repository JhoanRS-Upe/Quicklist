# Generated by Django 5.1.3 on 2024-11-24 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('claveA', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidoP', models.CharField(max_length=20)),
                ('apellidoM', models.CharField(max_length=20)),
                ('fechaNac', models.DateField()),
                ('estado', models.BooleanField()),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=2)),
                ('correo', models.EmailField(max_length=100)),
                ('contrasenia', models.CharField(max_length=128)),
                ('rango', models.CharField(choices=[('Administrador', 'Administrador')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('cuatrimestres', models.PositiveIntegerField()),
                ('alumnosEgre', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('idPeriodo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('inicial', models.CharField(max_length=1)),
                ('anio', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('correo', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(max_length=128)),
                ('estado', models.BooleanField(default=False)),
                ('rango', models.CharField(choices=[('Alumno', 'Alumno'), ('Profesor', 'Profesor'), ('Administrador', 'Administrador')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('matricula', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidoP', models.CharField(max_length=20)),
                ('apellidoM', models.CharField(max_length=20)),
                ('fechaNac', models.DateField()),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=2)),
                ('correo', models.EmailField(max_length=100)),
                ('contrasenia', models.CharField(max_length=128)),
                ('estado', models.BooleanField(default=False)),
                ('rango', models.CharField(choices=[('Alumno', 'Alumno')], max_length=30)),
                ('cbiometrico', models.CharField(max_length=100)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('grado', models.PositiveIntegerField()),
                ('grupo', models.CharField(max_length=1)),
                ('anio', models.PositiveIntegerField()),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='ClaseAlumno',
            fields=[
                ('idcAlumno', models.AutoField(primary_key=True, serialize=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno')),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clase')),
            ],
        ),
        migrations.CreateModel(
            name='ListaAsistencia',
            fields=[
                ('idLista', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('promedio', models.FloatField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('clave', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('creditos', models.PositiveIntegerField()),
                ('eje', models.CharField(max_length=30)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrera')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.periodo')),
            ],
        ),
        migrations.AddField(
            model_name='clase',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.materia'),
        ),
        migrations.AddField(
            model_name='clase',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.periodo'),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('clave', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidoP', models.CharField(max_length=20)),
                ('apellidoM', models.CharField(max_length=20)),
                ('fechaNac', models.DateField()),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=2)),
                ('grado', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=100)),
                ('contrasenia', models.CharField(max_length=128)),
                ('estado', models.BooleanField(default=False)),
                ('rango', models.CharField(choices=[('Profesor', 'Profesor')], max_length=20)),
                ('academia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.academia')),
            ],
        ),
        migrations.CreateModel(
            name='Justificante',
            fields=[
                ('idJustificante', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=20)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profesor')),
            ],
        ),
        migrations.AddField(
            model_name='clase',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profesor'),
        ),
        migrations.CreateModel(
            name='AlumnoLista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.CharField(max_length=1)),
                ('clase_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clasealumno')),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.listaasistencia')),
            ],
            options={
                'unique_together': {('lista', 'clase_alumno')},
            },
        ),
    ]
