# Generated by Django 5.0.7 on 2024-07-21 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_bread_nav_category_remove_fruits_nav_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bread',
        ),
        migrations.DeleteModel(
            name='Fruits',
        ),
        migrations.DeleteModel(
            name='Vegetables',
        ),
    ]
