# Generated by Django 5.0.3 on 2024-08-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_subcategory_options_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
