# Generated by Django 2.1.7 on 2019-03-05 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('address', models.CharField(blank=True, max_length=300)),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
        ),
    ]
