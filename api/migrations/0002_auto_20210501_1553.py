# Generated by Django 3.2 on 2021-05-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='latest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='video_data',
            name='thumbnail',
            field=models.TextField(),
        ),
    ]
