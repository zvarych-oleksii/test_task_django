# Generated by Django 5.0.1 on 2024-01-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_validation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailverificationresult',
            name='status',
            field=models.CharField(default='invalid', max_length=50),
        ),
    ]
