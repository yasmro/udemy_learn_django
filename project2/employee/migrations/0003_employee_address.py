# Generated by Django 2.2.16 on 2020-09-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20200922_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=20, verbose_name='住所'),
        ),
    ]