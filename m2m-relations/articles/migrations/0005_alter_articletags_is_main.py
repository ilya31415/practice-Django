# Generated by Django 4.0.3 on 2022-03-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_rename_id_article_articletags_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletags',
            name='is_main',
            field=models.BooleanField(null=True, verbose_name='Главный тег'),
        ),
    ]
