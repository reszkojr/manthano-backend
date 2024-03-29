# Generated by Django 4.2.6 on 2024-02-23 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManthanoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('username', models.CharField(max_length=32, verbose_name='Username')),
                ('first_name', models.CharField(max_length=32, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
            ],
            options={
                'verbose_name': 'username',
                'verbose_name_plural': 'usernames',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(null=True, upload_to='profile_images/')),
                ('profile_background', models.ImageField(null=True, upload_to='profile_backgrounds/')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
