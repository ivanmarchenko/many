# Generated by Django 3.0.7 on 2020-07-20 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_auto_20200717_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kerchnet_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ka_datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата-время создания')),
                ('ka_login', models.CharField(max_length=50, null=True, verbose_name='Логин')),
                ('ka_password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Юзер')),
            ],
            options={
                'verbose_name': 'Аккаунт керчьнет',
                'verbose_name_plural': 'Аккаунты керчьнета',
            },
        ),
        migrations.DeleteModel(
            name='Kerchent_account',
        ),
    ]
