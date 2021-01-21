# Generated by Django 3.1.3 on 2021-01-20 20:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='review',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]