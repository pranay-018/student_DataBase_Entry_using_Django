# Generated by Django 4.2.1 on 2023-05-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='srcmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_src', models.CharField(max_length=30)),
            ],
        ),
    ]
