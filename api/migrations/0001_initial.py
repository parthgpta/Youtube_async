# Generated by Django 3.2 on 2021-05-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('decription', models.TextField()),
                ('thumbnail', models.URLField(max_length=50)),
                ('published', models.TextField()),
            ],
        ),
    ]
