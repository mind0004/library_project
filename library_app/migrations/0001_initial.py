# Generated by Django 3.0.4 on 2020-03-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
