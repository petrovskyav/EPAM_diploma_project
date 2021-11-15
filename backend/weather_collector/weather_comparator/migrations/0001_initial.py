# Generated by Django 3.2.8 on 2021-11-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure_id', models.PositiveBigIntegerField()),
                ('datetime', models.DateTimeField()),
                ('min_temp', models.DecimalField(decimal_places=3, max_digits=7)),
                ('max_temp', models.DecimalField(decimal_places=3, max_digits=7)),
                ('the_temp', models.DecimalField(decimal_places=3, max_digits=7)),
                ('humidity', models.PositiveSmallIntegerField()),
            ],
        ),
    ]