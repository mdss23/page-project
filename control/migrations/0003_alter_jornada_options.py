# Generated by Django 4.1.6 on 2023-04-11 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jornada',
            options={'managed': False, 'ordering': ['id']},
        ),
    ]
