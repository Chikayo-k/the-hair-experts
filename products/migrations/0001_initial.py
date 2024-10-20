# Generated by Django 3.2.25 on 2024-08-19 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa
                ('name', models.CharField(max_length=150)),
                ('display_name', models.CharField(blank=True, max_length=150, null=True)), # noqa
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa
                ('sku', models.CharField(blank=True, max_length=100, null=True)), # noqa
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True)), # noqa
                ('image', models.ImageField(blank=True, null=True, upload_to='')), # noqa
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')), # noqa
            ],
        ),
    ]
