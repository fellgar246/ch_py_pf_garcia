# Generated by Django 4.2.5 on 2023-09-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogTecnoWave", "0006_alter_post_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="snippet",
            field=models.CharField(
                default="Da Click arriba para leer el post", max_length=255
            ),
        ),
    ]
