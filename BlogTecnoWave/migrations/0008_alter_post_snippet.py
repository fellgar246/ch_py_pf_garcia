# Generated by Django 4.2.5 on 2023-09-09 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogTecnoWave", "0007_post_snippet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="snippet",
            field=models.CharField(max_length=255),
        ),
    ]
