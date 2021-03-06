# Generated by Django 2.2 on 2021-02-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Created', 'Criado'), ('Progress', 'Pendente'), ('Done', 'Feito')], default='Created', max_length=20),
        ),
    ]
