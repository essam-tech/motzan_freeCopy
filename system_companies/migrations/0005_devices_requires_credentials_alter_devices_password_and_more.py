# Generated by Django 5.1.7 on 2025-03-12 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_companies', '0004_alter_devices_password_alter_devices_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='requires_credentials',
            field=models.BooleanField(default=False, verbose_name='يتطلب اسم مستخدم وكلمة مرور'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='كلمة المرور'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم المستخدم'),
        ),
    ]
