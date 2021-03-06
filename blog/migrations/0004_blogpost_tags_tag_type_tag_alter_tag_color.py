# Generated by Django 4.0.3 on 2022-05-09 16:56

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(related_name='blog_post', to='blog.tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='type_tag',
            field=models.CharField(choices=[('BLOG', 'Blog'), ('DIET', 'Diet ingredint')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=[('#FFFFFF', 'white'), ('#ff99cc', 'pink'), ('#ffb366', 'orange'), ('#4dff88', 'green'), ('#3399ff', 'blue'), ('#000066', 'navy'), ('#a64dff', 'purple'), ('#000000', 'black')]),
        ),
    ]
