# Generated by Django 5.1.7 on 2025-03-19 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0002_articletag_articlepage_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
