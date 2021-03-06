# Generated by Django 3.1.2 on 2020-10-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('First_Name', models.CharField(blank=True, max_length=100)),
                ('Middle_Name', models.CharField(blank=True, max_length=100)),
                ('Last_Name', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('Password', models.CharField(max_length=20)),
                ('Degree', models.CharField(blank=True, max_length=20)),
                ('Primary_Phone', models.CharField(blank=True, max_length=12)),
                ('Secondary_Email', models.EmailField(blank=True, max_length=254)),
                ('Department', models.CharField(blank=True, max_length=100)),
                ('Institution', models.CharField(blank=True, max_length=100)),
                ('Street_Address', models.CharField(blank=True, max_length=200)),
                ('City', models.CharField(blank=True, max_length=50)),
                ('State_Province', models.CharField(blank=True, max_length=100, verbose_name='State or Province')),
                ('Country', models.CharField(blank=True, max_length=20)),
                ('Zip_Postal_Code', models.CharField(blank=True, max_length=15)),
                ('Areas_of_Specialization', models.CharField(blank=True, max_length=200)),
                ('User_Type', models.CharField(blank=True, max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
