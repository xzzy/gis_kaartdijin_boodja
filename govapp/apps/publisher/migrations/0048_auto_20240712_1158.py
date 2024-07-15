# Generated by Django 3.2.25 on 2024-07-12 03:58

from django.db import migrations, models
import django.db.models.deletion
import govapp.apps.publisher.models.geoserver_roles_groups


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0047_geoservergroup_geoserver_usergroup_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoserverrole',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='geoservergroup',
            name='geoserver_usergroup_service',
            field=models.ForeignKey(blank=True, default=govapp.apps.publisher.models.geoserver_roles_groups.get_custom_usergroup_service, null=True, on_delete=django.db.models.deletion.CASCADE, to='publisher.geoserverusergroupservice'),
        ),
    ]