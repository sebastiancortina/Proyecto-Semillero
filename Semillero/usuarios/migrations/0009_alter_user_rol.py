# Generated by Django 4.0.5 on 2022-06-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_user_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.CharField(blank=True, default='estudiante', max_length=255, null=True),
        ),
    ]
