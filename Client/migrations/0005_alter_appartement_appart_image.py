# Generated by Django 4.2.1 on 2023-05-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0004_appartement_appart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartement',
            name='appart_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
