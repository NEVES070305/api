# Generated by Django 5.0.3 on 2024-03-13 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_clp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jsonclp',
            old_name='botao',
            new_name='Botao',
        ),
        migrations.RenameField(
            model_name='jsonclp',
            old_name='ligaRobo',
            new_name='LigaRobo',
        ),
        migrations.RenameField(
            model_name='jsonclp',
            old_name='resetContador',
            new_name='ResetContador',
        ),
        migrations.RenameField(
            model_name='jsonclp',
            old_name='sensor',
            new_name='Sensor',
        ),
        migrations.RenameField(
            model_name='jsonclp',
            old_name='valorContagem',
            new_name='Valor_Contagem',
        ),
    ]
