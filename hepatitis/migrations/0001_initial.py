# Generated by Django 4.0 on 2021-12-13 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hepatitis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=55, null=True)),
                ('email', models.CharField(default=None, max_length=55, null=True)),
                ('mobile', models.IntegerField(default=None, null=True)),
                ('age', models.IntegerField(default=None, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, null=True)),
                ('steroid', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('antivirals', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('fatigue', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('malaise', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('anorexia', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('liver_big', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('liver_firm', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('spleen_palpable', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('spiders', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('ascites', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('varices', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('bilirubin', models.FloatField(default=None, null=True)),
                ('alk_phosphate', models.FloatField(default=None, null=True)),
                ('sgot', models.FloatField(default=None, null=True)),
                ('albumin', models.FloatField(default=None, null=True)),
                ('protime', models.FloatField(default=None, null=True)),
                ('histology', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=6, null=True)),
                ('status', models.CharField(max_length=8, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
    ]
