# Generated by Django 2.2.5 on 2021-01-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StuData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('score', models.IntegerField()),
                ('type', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
