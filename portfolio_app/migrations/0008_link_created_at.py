# Generated by Django 4.2.5 on 2024-07-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0007_alter_link_profile_img_alter_link_resume_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
