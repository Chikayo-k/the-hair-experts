# Generated by Django 3.2.25 on 2024-10-01 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), # noqa
                ('review_title', models.CharField(max_length=20)),
                ('comment_area', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)), # noqa
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chosen_product', to='products.product')), # noqa
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]
