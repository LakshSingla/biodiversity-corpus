# Generated by Django 2.2.1 on 2019-07-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetsearch',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
