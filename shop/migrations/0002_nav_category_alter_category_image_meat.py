# Generated by Django 5.0.7 on 2024-07-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(allow_unicode=True, max_length=150, unique=True)),
                ('image', models.ImageField(upload_to='shop/nav_category')),
                ('price', models.FloatField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='shop/category'),
        ),
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('price', models.FloatField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nav_category', models.ManyToManyField(to='shop.nav_category')),
            ],
        ),
    ]
