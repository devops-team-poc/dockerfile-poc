# Generated by Django 2.2 on 2020-12-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201221_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubereatsoutlet',
            name='id_outlet',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='ubereatsoutlet',
            name='reviews_nr',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
