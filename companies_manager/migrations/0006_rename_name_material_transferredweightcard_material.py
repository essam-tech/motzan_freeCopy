# Generated by Django 5.1.4 on 2025-03-13 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies_manager', '0005_rename_material_transferredweightcard_name_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transferredweightcard',
            old_name='name_material',
            new_name='material',
        ),
    ]
