# Generated by Django 4.2.4 on 2023-08-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfile', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
