# Generated by Django 3.2.8 on 2022-06-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_service_field_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons/'),
        ),
    ]
