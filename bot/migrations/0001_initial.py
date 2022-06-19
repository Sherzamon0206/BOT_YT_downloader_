# Generated by Django 4.0.5 on 2022-06-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminid', models.IntegerField(blank=True, null=True, verbose_name='Admin id raqami')),
            ],
            options={
                'verbose_name': 'Admin:',
                'verbose_name_plural': 'AdminPanel',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exeterenal_id', models.PositiveIntegerField(verbose_name='user id')),
                ('username', models.TextField(blank=True, null=True, verbose_name='username')),
                ('f_name', models.TextField(verbose_name='First_name')),
                ('l_name', models.TextField(null=True, verbose_name='Lastname')),
            ],
            options={
                'verbose_name': 'Profili',
            },
        ),
    ]