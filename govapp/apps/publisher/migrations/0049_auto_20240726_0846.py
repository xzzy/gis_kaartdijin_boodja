# Generated by Django 3.2.25 on 2024-07-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0048_auto_20240712_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoserverpool',
            name='url_ui',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='geoserverrole',
            name='default',
            field=models.BooleanField(default=False, verbose_name='Default at geoserver'),
        ),
    ]
