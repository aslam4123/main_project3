# Generated by Django 4.2.16 on 2025-02-14 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='1', max_length=254),
            preserve_default=False,
        ),
    ]
