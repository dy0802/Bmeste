# Generated by Django 3.2.4 on 2021-06-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bmeste', '0004_auto_20210618_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece_detail',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='piece_detail',
            name='location_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='piece_detail',
            name='location_lng',
            field=models.FloatField(default=0),
        ),
    ]