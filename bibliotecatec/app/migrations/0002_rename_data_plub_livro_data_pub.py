# Generated by Django 4.2.5 on 2023-09-15 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='data_plub',
            new_name='data_pub',
        ),
    ]
