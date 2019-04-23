# Generated by Django 2.1.7 on 2019-04-10 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_auto_20190410_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
