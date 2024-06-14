# Generated by Django 5.0.3 on 2024-06-05 21:33

import django.db.models.deletion
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
                ('baner', models.ImageField(upload_to='baner_category')),
                ('is_sub', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('sub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='content.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('baner', models.ImageField(upload_to='baner_products/')),
                ('price', models.IntegerField()),
                ('is_avalable', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(related_name='product_category', to='content.category')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='GaleryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='galery_products/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galery', to='content.product')),
            ],
        ),
    ]
