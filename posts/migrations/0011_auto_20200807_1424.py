# Generated by Django 3.0.7 on 2020-08-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20200807_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Содержимое'),
        ),
    ]