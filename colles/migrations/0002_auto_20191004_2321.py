# Generated by Django 2.0.7 on 2019-10-04 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colle',
            name='creneau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colles.creneau'),
        ),
        migrations.AlterField(
            model_name='colle',
            name='groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colles.groupe'),
        ),
        migrations.AlterField(
            model_name='colleur',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userc', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creneau',
            name='colleur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colles.colleur'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usere', to=settings.AUTH_USER_MODEL),
        ),
    ]
