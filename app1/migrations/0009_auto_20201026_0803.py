# Generated by Django 3.1.2 on 2020-10-26 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20201025_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockupload',
            name='manuscript_key',
            field=models.CharField(blank=True, default='key-837920894', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='manuscript_detail',
            name='upload_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 26, 8, 3, 7, 913899)),
        ),
    ]
