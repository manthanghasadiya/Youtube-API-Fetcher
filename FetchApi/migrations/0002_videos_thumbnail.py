# Generated by Django 3.2.9 on 2022-04-19 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FetchApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='thumbnail',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
