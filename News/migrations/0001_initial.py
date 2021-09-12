# Generated by Django 3.2.7 on 2021-09-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('pubtime', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
                ('press', models.IntegerField(default=0)),
            ],
        ),
    ]