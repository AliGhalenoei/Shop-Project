# Generated by Django 5.0.3 on 2024-06-30 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_product_sub_category_remove_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_sub',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
    ]
