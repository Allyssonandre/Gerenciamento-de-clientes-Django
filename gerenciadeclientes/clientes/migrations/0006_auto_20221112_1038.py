# Generated by Django 3.1.6 on 2022-11-12 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20221102_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienteconta',
            name='conta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente', verbose_name='Conta do cliente:'),
        ),
    ]
