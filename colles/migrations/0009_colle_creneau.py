# Generated by Django 2.0.7 on 2019-10-05 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colles', '0008_auto_20191005_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='colle',
            name='creneau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='colles.creneau'),
        ),
    ]
