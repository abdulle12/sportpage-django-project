# Generated by Django 5.0.6 on 2024-06-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0013_transfepage3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfepage4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
                ('urls', models.CharField(max_length=100)),
            ],
        ),
    ]
