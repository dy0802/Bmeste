# Generated by Django 3.2.4 on 2021-06-13 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bmeste', '0002_auto_20210613_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='title',
        ),
        migrations.CreateModel(
            name='Pieces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bmeste.author')),
            ],
        ),
    ]