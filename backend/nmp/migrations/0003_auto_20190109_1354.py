# Generated by Django 2.1.2 on 2019-01-09 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmp', '0002_auto_20190109_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmparcelcropneeds',
            name='priority_order',
            field=models.FloatField(),
        ),
    ]
