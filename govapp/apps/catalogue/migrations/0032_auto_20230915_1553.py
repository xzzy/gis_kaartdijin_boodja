# Generated by Django 3.2.20 on 2023-09-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0031_add_last_job_run'),
    ]

    operations = [
        migrations.AddField(
            model_name='layersubmission',
            name='layer_attribute',
            field=models.TextField(blank=True, help_text='This is the attribute data from the spatial file.', null=True),
        ),
        migrations.AlterField(
            model_name='customqueryfrequency',
            name='last_job_run',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
