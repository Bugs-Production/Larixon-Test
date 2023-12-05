# Generated by Django 5.0 on 2023-12-04 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'город объявлений',
                'verbose_name_plural': 'Город объявлений',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорию объявлений', 'verbose_name_plural': 'Категория объявлений'},
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category', verbose_name='Категория объявления')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city', verbose_name='Город для объявления')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
