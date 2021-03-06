# Generated by Django 2.0.3 on 2018-03-22 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('brand', models.CharField(blank=True, max_length=225, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(default=django.utils.timezone.now)),
                ('colors', models.CharField(blank=True, choices=[('White', '#FFFFFF'), ('Black', '#000000'), ('Red', '#ff0000'), ('Blue', '#0000ff'), ('Green', '#008000'), ('Yellow', '#FFFF00'), ('Orange', '#FFA500'), ('Brown', '#A52A2A')], default='#000000', max_length=225, null=True)),
                ('qr_code', models.CharField(blank=True, max_length=225, null=True)),
                ('barcode', models.CharField(blank=True, max_length=225, null=True)),
                ('isSold', models.BooleanField(default=False)),
            ],
        ),
    ]
