# Generated by Django 5.0.1 on 2024-01-20 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_tbl_location'),
        ('Guest', '0004_alter_tbl_towingagent_agent_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=30)),
                ('user_contact', models.CharField(max_length=15)),
                ('user_address', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=20)),
                ('user_photo', models.FileField(upload_to='UserDoc/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]