# Generated by Django 2.2.28 on 2024-03-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0009_auto_20240320_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='profile_images/placeholder.jpg', upload_to='profile_images'),
        ),
    ]