# Generated by Django 2.1.1 on 2018-09-08 10:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('read_statistics', '0002_auto_20180908_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('read_num', models.IntegerField(default=0)),
                ('object_id', models.PositiveIntegerField()),
                ('contenttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
