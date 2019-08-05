# Generated by Django 2.2.2 on 2019-08-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField()),
                ('summary', models.CharField(max_length=10000)),
            ],
        ),
    ]