# Generated by Django 3.1 on 2021-01-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laporan',
            old_name='dilaporkan',
            new_name='id_dilaporkan',
        ),
        migrations.RenameField(
            model_name='laporan',
            old_name='pelapor',
            new_name='id_pelapor',
        ),
        migrations.RemoveField(
            model_name='laporan',
            name='user_field',
        ),
        migrations.AddField(
            model_name='laporan',
            name='asrama',
            field=models.CharField(default='Belum diatur', max_length=8),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nama',
            field=models.CharField(default='UnNamed', max_length=64),
        ),
    ]
