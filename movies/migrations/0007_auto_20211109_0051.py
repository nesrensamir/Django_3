# Generated by Django 3.2.9 on 2021-11-09 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default=0, max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='cast',
            name='id_number',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='movies.idnumber'),
            preserve_default=False,
        ),
    ]
