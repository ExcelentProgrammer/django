# Generated by Django 5.0.2 on 2024-02-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('http', '0005_alter_post_desc_alter_post_desc_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
