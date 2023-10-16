# Generated by Django 4.2.6 on 2023-10-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='code',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='description',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='schedule',
            field=models.ImageField(null=True, upload_to='uploads/schedule_%Y_%m_%d'),
        ),
    ]
