# Generated by Django 4.1.7 on 2023-03-11 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_exemple_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Narxnoma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=20)),
                ('narxi', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='exemple',
            name='name',
        ),
        migrations.AddField(
            model_name='exemple',
            name='summa',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='exemple',
            name='narxnoma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='login.narxnoma'),
        ),
    ]
