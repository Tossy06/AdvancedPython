# Generated by Django 5.1.5 on 2025-01-17 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrudapp', '0005_rename_notas_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.TextField(max_length=200),
        ),
    ]