# Generated by Django 3.2.8 on 2024-02-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaunaInfo',
            fields=[
                ('SaunaId', models.IntegerField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('StoreName', models.CharField(max_length=255)),
                ('ColdBathRating', models.IntegerField()),
                ('SaunaRating', models.IntegerField()),
                ('IndoorOutdoorRating', models.IntegerField()),
                ('access', models.CharField(max_length=255)),
                ('SaunaReview', models.CharField(max_length=255)),
                ('StoreImage', models.BinaryField()),
            ],
        ),
        migrations.DeleteModel(
            name='sauna_info',
        ),
    ]
