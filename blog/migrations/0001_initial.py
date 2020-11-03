# Generated by Django 3.1.2 on 2020-11-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
