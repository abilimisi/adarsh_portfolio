# Generated by Django 4.2.5 on 2024-07-07 09:30

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0011_name_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_Known',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=100)),
                ('work_desc', tinymce.models.HTMLField()),
            ],
        ),
    ]
