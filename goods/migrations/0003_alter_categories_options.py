# Generated by Django 5.1.4 on 2025-01-29 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_options_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('id',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
