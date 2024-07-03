# Generated by Django 5.0.6 on 2024-07-01 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0037_news_article_9_paragraph1i'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer_article_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('p1', models.CharField(max_length=1000)),
                ('p2', models.CharField(max_length=1000)),
                ('img', models.ImageField(upload_to='pic')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('Transfer_article_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='sportapp.transfer_article_1')),
            ],
        ),
    ]