# Generated by Django 5.1.7 on 2025-03-11 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='requires_credentials',
            field=models.BooleanField(default=False, verbose_name='تتطلب اسم مستخدم وكلمة مرور'),
        ),
    ]
