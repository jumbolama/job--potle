# Generated by Django 2.2.2 on 2020-02-24 09:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('count', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=255, null=True)),
                ('location', models.CharField(max_length=150)),
                ('company_name', models.CharField(max_length=100)),
                ('company_description', models.TextField()),
                ('website', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_date', models.DateTimeField()),
                ('filled', models.BooleanField(default=False)),
                ('salary', models.IntegerField(blank=True, default=0)),
                ('category', models.ManyToManyField(related_name='job_categoreis', to='job_app.Category')),
            ],
        ),
    ]
