# Generated by Django 2.1.2 on 2018-11-04 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20181103_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentcard',
            name='name',
            field=models.CharField(blank=True, help_text='Enter a name for this payment, up to 32 characters!', max_length=32, null=True, verbose_name='Card Name: '),
        ),
    ]
