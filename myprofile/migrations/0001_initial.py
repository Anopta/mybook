# Generated by Django 4.0.5 on 2022-07-21 04:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myprofile.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=255, null=True)),
                ('course', models.CharField(max_length=255, null=True)),
                ('admission_date', models.DateField(null=True)),
                ('graduation_date', models.DateField(null=True)),
                ('grade', models.FloatField(max_length=255, null=True)),
                ('graduation_type', models.FloatField(max_length=255, null=True)),
                ('thesis', models.CharField(max_length=255, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myprofile.profile')),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
    ]
