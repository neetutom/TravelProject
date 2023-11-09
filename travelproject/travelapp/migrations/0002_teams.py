# Generated by Django 4.2.6 on 2023-10-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('member_image', models.ImageField(upload_to='pics')),
                ('member_description', models.TextField()),
            ],
        ),
    ]