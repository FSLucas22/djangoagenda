# Generated by Django 4.1.5 on 2023-02-01 18:52

import core.rules.constants
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evento_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegraRepeticao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_regra', models.IntegerField(choices=[(core.rules.constants.TipoRepeticao['TODO_DIA'], 1), (core.rules.constants.TipoRepeticao['TODA_SEMANA'], 2), (core.rules.constants.TipoRepeticao['TODO_MES'], 3), (core.rules.constants.TipoRepeticao['TODO_ANO'], 4), (core.rules.constants.TipoRepeticao['TODO_DIA_UTIL'], 5), (core.rules.constants.TipoRepeticao['A_CADA_PERIODO'], 6)])),
                ('vezes', models.IntegerField(default=-1)),
                ('periodo', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='regra_repeticao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.regrarepeticao'),
        ),
    ]
