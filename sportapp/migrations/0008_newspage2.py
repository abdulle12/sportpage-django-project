# Generated by Django 5.0.6 on 2024-06-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0007_rename_newspage_newspage1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newspage2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
                ('urls', models.CharField(max_length=100)),
            ],
        ),
    ]
