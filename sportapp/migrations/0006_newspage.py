# Generated by Django 5.0.6 on 2024-06-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0005_homepage3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newspage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
                ('urls', models.CharField(max_length=100)),
            ],
        ),
    ]
