# Generated by Django 2.2 on 2020-12-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201221_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripadvisoroutlet',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
