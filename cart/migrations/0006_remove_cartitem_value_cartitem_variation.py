# Generated by Django 4.0.1 on 2022-03-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_remove_variation_image_remove_variation_value_value'),
        ('cart', '0005_remove_cartitem_variation_value_cartitem_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='value',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]