# Generated by Django 4.0 on 2021-12-15 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=55, null=True)),
                ('email', models.CharField(default=None, max_length=55, null=True)),
                ('age', models.IntegerField(default=None, null=True)),
                ('texture_mean', models.FloatField(default=None, null=True)),
                ('area_mean', models.FloatField(default=None, null=True)),
                ('smoothness_mean', models.FloatField(default=None, null=True)),
                ('compactness_mean', models.FloatField(default=None, null=True)),
                ('concavity_mean', models.FloatField(default=None, null=True)),
                ('concave_points_mean', models.FloatField(default=None, null=True)),
                ('state', models.FloatField(default=None, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
    ]
