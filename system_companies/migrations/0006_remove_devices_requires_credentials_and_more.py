# Generated by Django 5.1.7 on 2025-03-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_companies', '0005_devices_requires_credentials_alter_devices_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='requires_credentials',
        ),
        migrations.AlterField(
            model_name='devices',
            name='baud_rate',
            field=models.CharField(choices=[('9600', '9600'), ('19200', '19200'), ('38400', '38400'), ('57600', '57600'), ('115200', '115200')], default='9600', max_length=50, verbose_name='معدل الباود'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='initialization_data_size',
            field=models.PositiveIntegerField(choices=[(5, '5'), (6, '6'), (7, '7'), (8, '8')], default=8, verbose_name='حجم بيانات التهيئة'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='number_of_initialization_bits',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2')], default=1, verbose_name='عدد بتات التهيئة'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='كلمة المرور'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='اسم المستخدم'),
        ),
    ]
