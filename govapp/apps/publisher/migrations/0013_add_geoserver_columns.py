# Generated by Django 3.2.20 on 2023-08-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0012_geoserverpool'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='active',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='llb_crs',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='llb_maxx',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='llb_maxy',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='llb_minx',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='llb_miny',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='nbb_crs',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='nbb_maxx',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='nbb_maxy',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='nbb_minx',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='nbb_miny',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='geoserverpublishchannel',
            name='srs',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
