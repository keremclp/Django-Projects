# Generated by Django 4.2 on 2023-05-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
