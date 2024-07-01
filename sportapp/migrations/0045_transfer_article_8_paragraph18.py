# Generated by Django 5.0.6 on 2024-07-01 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0044_transfer_article_7_paragraph17'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer_article_8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('p1', models.CharField(max_length=1000)),
                ('p2', models.CharField(max_length=1000)),
                ('img', models.ImageField(upload_to='pic')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph18',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('Transfer_article_8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='sportapp.transfer_article_8')),
            ],
        ),
    ]
