# Generated by Django 3.1.6 on 2022-11-02 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20221101_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienteconta',
            name='conta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente', verbose_name='Conta do cliente:'),
        ),
    ]