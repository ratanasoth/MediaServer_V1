# Generated by Django 2.2.6 on 2019-10-16 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20191016_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='collections',
        ),
        migrations.AddField(
            model_name='movie',
            name='collections',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Collection'),
        ),
    ]
