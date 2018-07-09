# Generated by Django 2.0.5 on 2018-06-14 06:15

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightSaltUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modifiy_time', models.DateTimeField(auto_now=True)),
                ('member_id', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True)),
                ('name', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('member_type_code', models.CharField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'LSMB001M',
            },
        ),
        migrations.CreateModel(
            name='LightSaltPastor',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modifiy_time', models.DateTimeField(auto_now=True)),
                ('church_no', models.AutoField(primary_key=True, serialize=False)),
                ('pastor_id', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True)),
                ('church_name', models.CharField(max_length=100)),
                ('graduation_proof', models.ImageField(null=True, upload_to='')),
                ('church_satification', models.ImageField(null=True, upload_to='')),
                ('church_type_code', models.CharField(max_length=10)),
                ('church_post', models.CharField(max_length=10)),
                ('church_address', models.CharField(max_length=300)),
                ('authentication_yn', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'LSMB002M',
            },
            managers=[
                ('objects', account.models.LightSaltPastorManager()),
            ],
        ),
    ]
