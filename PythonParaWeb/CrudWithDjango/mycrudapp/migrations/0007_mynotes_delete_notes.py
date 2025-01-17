# Generated by Django 5.1.5 on 2025-01-17 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycrudapp', '0006_alter_notes_content_alter_notes_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycrudapp.users')),
            ],
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]
