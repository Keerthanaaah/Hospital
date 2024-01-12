# Generated by Django 4.2.6 on 2023-11-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Masteraccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('contactnum', models.CharField(max_length=150)),
                ('mail', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('confirmpassword', models.CharField(max_length=150)),
            ],
        ),
    ]
