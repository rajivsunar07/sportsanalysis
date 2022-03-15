# Generated by Django 4.0.3 on 2022-03-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures',
            name='event',
            field=models.FloatField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='ftr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='kickoff_time',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='started',
            field=models.BooleanField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='team_a_score',
            field=models.FloatField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='team_h_score',
            field=models.FloatField(max_length=250, null=True),
        ),
    ]
