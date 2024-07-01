# Generated by Django 5.0.6 on 2024-06-30 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0030_news_article_2_paragraph1b'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_article_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('p1', models.CharField(max_length=1000)),
                ('p2', models.CharField(max_length=1000)),
                ('img', models.ImageField(upload_to='pic')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph1c',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('News_article_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='sportapp.news_article_3')),
            ],
        ),
    ]
