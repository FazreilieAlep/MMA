# Generated by Django 5.0.6 on 2024-05-26 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=200)),
                ('acronyms', models.CharField(default=None, max_length=20, null=True)),
                ('domain_name', models.CharField(max_length=200, unique=True)),
                ('path', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MyGovEconomicIndicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('lagging', models.DecimalField(decimal_places=2, max_digits=10)),
                ('leading', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coincident', models.DecimalField(decimal_places=2, max_digits=10)),
                ('leading_diffusion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coincident_diffusion', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='MyGovHouseholdIncomeAndExpenditureStates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('state', models.CharField(max_length=20)),
                ('expenditure_mean', models.IntegerField()),
                ('income_median', models.IntegerField()),
                ('income_mean', models.IntegerField()),
                ('gini', models.DecimalField(decimal_places=8, max_digits=20)),
                ('poverty', models.DecimalField(decimal_places=2, default=-0.0, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='MyGovHouseholdIncomebyPercentile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('percentile', models.IntegerField()),
                ('variable', models.CharField(max_length=8)),
                ('income', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyGovMonetoryAggregates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('measure', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Web_API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=200, null=True)),
                ('path', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=200)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.host')),
            ],
        ),
    ]
