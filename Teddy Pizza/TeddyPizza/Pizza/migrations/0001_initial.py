# Generated by Django 3.0.8 on 2021-02-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientList',
            fields=[
                ('ingredient_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(default='', max_length=50)),
                ('pizza_name', models.CharField(max_length=50)),
                ('price', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
