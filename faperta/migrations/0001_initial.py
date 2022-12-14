# Generated by Django 4.1 on 2022-10-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('NIP', models.CharField(max_length=40)),
                ('tanggal_lahir', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('fakultas', models.CharField(max_length=40)),
                ('prodi', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('NIM', models.CharField(max_length=40)),
                ('tanggal_lahir', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('fakultas', models.CharField(max_length=40)),
                ('prodi', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('NIP', models.CharField(max_length=40)),
                ('tanggal_lahir', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('unit', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=40)),
            ],
        ),
    ]
