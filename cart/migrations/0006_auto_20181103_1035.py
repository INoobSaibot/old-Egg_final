# Generated by Django 2.1.2 on 2018-11-03 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20181103_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcart',
            name='cartOwner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]