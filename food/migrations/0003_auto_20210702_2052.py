# Generated by Django 3.2.5 on 2021-07-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20210522_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='foodenergy',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
