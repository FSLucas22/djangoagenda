# Generated by Django 4.1.5 on 2023-02-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_regrarepeticao_evento_regra_repeticao'),
    ]

    operations = [
        migrations.AddField(
            model_name='regrarepeticao',
            name='flag_fevereiro_29',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='regrarepeticao',
            name='flag_ir_para_marco',
            field=models.BooleanField(default=False),
        ),
    ]
