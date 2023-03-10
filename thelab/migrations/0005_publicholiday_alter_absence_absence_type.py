# Generated by Django 4.1.4 on 2022-12-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thelab', '0004_absence_absence_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicHoliday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='absence',
            name='absence_type',
            field=models.CharField(choices=[('HO', 'Home Office'), ('O', 'Office'), ('V', 'Vacation'), ('F', 'Flex Time'), ('PL', 'Parental Leave')], max_length=200),
        ),
    ]
