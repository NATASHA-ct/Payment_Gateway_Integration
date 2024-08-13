# Generated by Django 5.0.8 on 2024-08-08 14:50

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
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('file', models.FileField(blank=True, null=True, upload_to='product_files/')),
                ('url', models.URLField()),
            ],
        ),
    ]
