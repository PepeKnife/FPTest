# Generated by Django 4.2.2 on 2023-06-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sara_website', '0003_remove_abt_carousel_name_abt_carousel_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='abt_description',
            name='name',
            field=models.CharField(default='description', max_length=50),
        ),
    ]
