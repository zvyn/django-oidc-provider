# Generated by Django 4.2 on 2024-10-03 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0026_client_multiple_response_types'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rsakey',
            options={'ordering': ['id'], 'verbose_name': 'RSA Key', 'verbose_name_plural': 'RSA Keys'},
        ),
    ]