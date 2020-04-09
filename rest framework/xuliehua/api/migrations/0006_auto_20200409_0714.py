# Generated by Django 2.2.6 on 2020-04-08 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200409_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordetail',
            name='author',
            field=models.OneToOneField(db_constraint=False, default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='detail', to='api.Author'),
        ),
    ]
