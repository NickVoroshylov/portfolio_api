# Generated by Django 3.2.4 on 2021-06-04 10:01

from django.db import migrations, models
import portfolios.models.picture


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0003_picture_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to=portfolios.models.picture.portfolio_directory_path),
        ),
    ]