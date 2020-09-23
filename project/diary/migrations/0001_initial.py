# Generated by Django 2.2.16 on 2020-09-21 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
    ]