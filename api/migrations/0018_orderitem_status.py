# Generated by Django 3.0.8 on 2020-12-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20201209_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSED', 'Processed'), ('ARCHIVED', 'Archived')], default='PENDING', max_length=20, verbose_name='status'),
        ),
    ]
