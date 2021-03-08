# Generated by Django 3.1.5 on 2021-02-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210217_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reagentsfile',
            name='reagent',
        ),
        migrations.AddField(
            model_name='reagent',
            name='file',
            field=models.ManyToManyField(to='products.ReagentsFile'),
        ),
        migrations.AddField(
            model_name='reagentsfile',
            name='photo_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='название фото, не обязательно'),
        ),
        migrations.AlterField(
            model_name='reagentsfile',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Указать реагент, для которого добавлено фото/видео'),
        ),
    ]
