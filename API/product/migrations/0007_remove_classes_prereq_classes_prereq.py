# Generated by Django 4.0.3 on 2022-04-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_classes_coreq_alter_classes_prereq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='prereq',
        ),
        migrations.AddField(
            model_name='classes',
            name='prereq',
            field=models.ManyToManyField(blank=True, null=True, related_name='prereqclass', to='product.classes'),
        ),
    ]
