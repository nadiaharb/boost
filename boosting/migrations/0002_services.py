# Generated by Django 3.2.6 on 2022-01-27 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boosting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boosting.division')),
            ],
        ),
    ]
