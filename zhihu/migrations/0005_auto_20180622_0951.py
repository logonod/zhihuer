# Generated by Django 2.0.3 on 2018-06-22 09:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zhihu', '0004_answercomment_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='话题描述'),
        ),
        migrations.AddField(
            model_name='topic',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='用户话题'),
        ),
    ]
