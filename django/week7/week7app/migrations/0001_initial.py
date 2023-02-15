# Generated by Django 4.1.6 on 2023-02-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('employee', models.IntegerField()),
            ],
        ),
    ]
