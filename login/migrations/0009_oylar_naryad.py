# Generated by Django 4.1.7 on 2023-03-12 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_qabul'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oylar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Naryad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.FloatField()),
                ('summa', models.FloatField()),
                ('hodim', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.qabul')),
                ('narxnoma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.narxnoma')),
                ('oylar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='login.oylar')),
            ],
        ),
    ]
