# Generated by Django 2.0.7 on 2019-10-04 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='colle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semaine', models.IntegerField(default=1)),
                ('note1', models.IntegerField(null=True)),
                ('note2', models.IntegerField(null=True)),
                ('note3', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='colleur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matière', models.CharField(choices=[('M', 'Maths'), ('P', 'Physique')], default='M', max_length=1)),
                ('civilité', models.CharField(choices=[('M.', 'Monsieur'), ('Mme', 'Madame')], default='M.', max_length=3)),
                ('tel', models.CharField(blank=True, default='', max_length=20)),
                ('user', models.OneToOneField(on_delete='CASCADE', related_name='userc', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='creneau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.IntegerField(choices=[(1, 'lundi'), (2, 'mardi'), (3, 'mercredi'), (4, 'jeudi'), (5, 'vendredi'), (6, 'samedi')], default=1)),
                ('heure', models.IntegerField()),
                ('duree', models.IntegerField(default=1)),
                ('colleur', models.ForeignKey(on_delete='CASCADE', to='colles.colleur')),
            ],
        ),
        migrations.CreateModel(
            name='eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, max_length=255, null=True, upload_to='trombi/', verbose_name='Trombine')),
                ('tel', models.CharField(blank=True, default='', max_length=20)),
                ('civilité', models.CharField(choices=[('M.', 'Monsieur'), ('Mme', 'Madame')], default='M.', max_length=3)),
                ('user', models.OneToOneField(on_delete='CASCADE', related_name='usere', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=3)),
                ('el1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='el1', to=settings.AUTH_USER_MODEL)),
                ('el2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='el2', to=settings.AUTH_USER_MODEL)),
                ('el3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='el3', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='colle',
            name='creneau',
            field=models.ForeignKey(on_delete='CASCADE', to='colles.creneau'),
        ),
        migrations.AddField(
            model_name='colle',
            name='groupe',
            field=models.ForeignKey(on_delete='CASCADE', to='colles.groupe'),
        ),
    ]