# Generated by Django 2.0.3 on 2018-06-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhihu', '0008_question_is_anonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_anonymous',
            field=models.BooleanField(default=False, verbose_name='匿名回答'),
        ),
    ]
