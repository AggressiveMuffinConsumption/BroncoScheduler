# Generated by Django 4.0.3 on 2022-04-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_classes_prereq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='prereq',
            field=models.ManyToManyField(blank=True, to='product.classes'),
        ),
    ]