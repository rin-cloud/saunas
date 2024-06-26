# Generated by Django 3.2.8 on 2024-02-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sauna_info',
            fields=[
                ('sauna_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('store_name', models.CharField(max_length=255)),
                ('cold_bath_rating', models.IntegerField()),
                ('sauna_rating', models.IntegerField()),
                ('indoor_outdoor_rating', models.IntegerField()),
                ('access', models.CharField(max_length=255)),
                ('sauna_review', models.CharField(max_length=255)),
                ('store_image', models.BinaryField()),
            ],
        ),
    ]
