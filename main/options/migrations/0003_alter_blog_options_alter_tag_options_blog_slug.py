# Generated by Django 5.0.3 on 2024-07-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0002_tag_alter_story_options_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id'], 'verbose_name': 'افزودن بلاگ ', 'verbose_name_plural': 'بلاگ ها'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id'], 'verbose_name': 'افزودن برچسب ', 'verbose_name_plural': 'برچسب ها'},
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
