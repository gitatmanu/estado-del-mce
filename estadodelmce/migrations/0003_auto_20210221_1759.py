# Generated by Django 2.2.17 on 2021-02-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadodelmce', '0002_communistparty_trend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communistparty',
            name='foundation_date',
            field=models.DateField(),
        ),
    ]