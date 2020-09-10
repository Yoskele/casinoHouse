# Generated by Django 3.1.1 on 2020-09-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('meta_title', models.CharField(blank=True, max_length=100)),
                ('meta_description', models.TextField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('casinoLogo', models.ImageField(blank=True, upload_to='casinoLogo')),
                ('affiliate_link', models.CharField(blank=True, max_length=500)),
                ('warningLabel', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='GameSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('meta_title', models.CharField(blank=True, max_length=100)),
                ('meta_description', models.TextField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('gameSupplierLogo', models.ImageField(blank=True, upload_to='gameSupplier')),
            ],
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='image',
            field=models.ImageField(blank=True, upload_to='articleImages'),
        ),
    ]