# Generated by Django 4.2.5 on 2024-07-07 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='profile_img',
            field=models.ImageField(upload_to='profileimage'),
        ),
        migrations.AlterField(
            model_name='link',
            name='resume_file',
            field=models.FileField(upload_to='resume'),
        ),
    ]
