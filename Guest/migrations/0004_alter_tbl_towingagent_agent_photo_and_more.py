# Generated by Django 5.0.1 on 2024-01-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_tbl_towingagent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_towingagent',
            name='agent_photo',
            field=models.FileField(upload_to='AgentDoc/'),
        ),
        migrations.AlterField(
            model_name='tbl_towingagent',
            name='agent_proof',
            field=models.FileField(upload_to='AgentDoc/'),
        ),
    ]