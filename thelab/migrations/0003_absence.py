# Generated by Django 4.1.4 on 2022-12-22 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thelab', '0002_teammember_initials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.DateField()),
                ('end_date', models.DateField()),
                ('teammember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thelab.teammember')),
            ],
        ),
    ]
