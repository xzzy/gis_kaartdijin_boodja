# Generated by Django 3.2.25 on 2024-05-02 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0031_alter_geoserverpublishchannel_publish_entry'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='geoserverpublishchannel',
            unique_together={('publish_entry', 'geoserver_pool')},
        ),
    ]