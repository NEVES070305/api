# Generated by Django 5.0.3 on 2024-03-13 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JSONCLP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.BooleanField()),
                ('botao', models.BooleanField()),
                ('ligaRobo', models.BooleanField()),
                ('resetContador', models.BooleanField()),
                ('valorContagem', models.IntegerField()),
            ],
        ),
    ]
