# Generated by Django 4.0.3 on 2022-05-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='publish date'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(help_text='Steps separator is semi-colon', verbose_name='instructions'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
    ]
