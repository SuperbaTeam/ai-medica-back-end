# Generated by Django 4.0 on 2021-12-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stroke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=55, null=True)),
                ('email', models.CharField(default=None, max_length=55, null=True)),
                ('mobile', models.IntegerField(default=None, null=True)),
                ('age', models.IntegerField(default=None, null=True)),
                ('bmi', models.FloatField(default=None, null=True)),
                ('avg_glucose_level', models.FloatField(default=None, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, null=True)),
                ('residence_type', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5, null=True)),
                ('ever_married', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5, null=True)),
                ('work_type', models.CharField(choices=[('govt_job', 'govt_job'), ('never_worked', 'never_worked'), ('private', 'private'), ('self-employed', 'Self-employed'), ('self-employed', 'children')], default='never_worked', max_length=32, null=True)),
                ('smoking_status', models.CharField(choices=[('unknown', 'unknown'), ('formerly_smoked', 'formerly_smoked'), ('never_smoked', 'never_smoked'), ('smokes', 'smokes')], default='unknown', max_length=32, null=True)),
                ('hypertension', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5, null=True)),
                ('heart_disease', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5, null=True)),
                ('status', models.CharField(max_length=8, null=True)),
            ],
        ),
    ]