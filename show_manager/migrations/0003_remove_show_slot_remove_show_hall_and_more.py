# Generated by Django 5.1.2 on 2024-11-12 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_manager', '0002_alter_show_category_alter_show_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='slot',
        ),
        migrations.RemoveField(
            model_name='show',
            name='hall',
        ),
        migrations.RemoveField(
            model_name='show',
            name='show_producer',
        ),
        migrations.DeleteModel(
            name='Slot',
        ),
    ]
