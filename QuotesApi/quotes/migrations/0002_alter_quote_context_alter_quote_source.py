# Generated by Django 4.2.1 on 2023-05-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='context',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.URLField(max_length=50),
        ),
    ]