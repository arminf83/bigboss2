# Generated by Django 5.1 on 2024-09-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_born_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='personal_code',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]