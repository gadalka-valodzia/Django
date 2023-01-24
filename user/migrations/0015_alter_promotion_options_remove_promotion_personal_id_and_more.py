# Generated by Django 4.1.5 on 2023-01-24 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_contract_options_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promotion',
            options={'verbose_name': 'Поощрение', 'verbose_name_plural': 'Поощрения'},
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='personal_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='promotion',
        ),
        migrations.AddField(
            model_name='promotion',
            name='personal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user', verbose_name='Сотрудник'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promotion',
            field=models.CharField(max_length=40, verbose_name='Поощрение'),
        ),
    ]
