# Generated by Django 2.1.7 on 2019-04-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_auto_20190415_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
