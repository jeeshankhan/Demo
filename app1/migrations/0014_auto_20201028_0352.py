# Generated by Django 3.1.2 on 2020-10-28 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_auto_20201027_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_heading', models.CharField(blank=True, max_length=100, null=True)),
                ('paragraf', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dockupload',
            name='manuscript_key',
            field=models.CharField(blank=True, default='key-35236927137', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='manuscript_detail',
            name='upload_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 28, 3, 52, 36, 920139)),
        ),
    ]
