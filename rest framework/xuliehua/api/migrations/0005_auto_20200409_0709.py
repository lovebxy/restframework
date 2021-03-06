# Generated by Django 2.2.6 on 2020-04-08 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200408_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordetail',
            name='author',
            field=models.OneToOneField(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detail', to='api.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(db_constraint=False, related_name='books', to='api.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='public',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='api.Publish'),
        ),
    ]
