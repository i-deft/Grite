# Generated by Django 3.1.5 on 2021-02-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_division_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='description',
            field=models.CharField(blank=True, max_length=300, verbose_name='Описаниее направления'),
        ),
        migrations.AlterField(
            model_name='division',
            name='photo',
            field=models.FileField(upload_to='products/%Y/%m/%d/'),
        ),
    ]
