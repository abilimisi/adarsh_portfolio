# Generated by Django 4.2.5 on 2024-07-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0008_link_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
