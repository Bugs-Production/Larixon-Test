# Generated by Django 5.0 on 2023-12-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория объявлений',
                'verbose_name_plural': 'Категории объявлений',
            },
        ),
    ]