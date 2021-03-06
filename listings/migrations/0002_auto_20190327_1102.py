# Generated by Django 2.1.7 on 2019-03-27 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='research_paper_txt',
            field=models.FileField(blank=True, upload_to='research_papers/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='researcher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='researchers.Researcher'),
        ),
    ]
