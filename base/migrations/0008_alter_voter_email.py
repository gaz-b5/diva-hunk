# Generated by Django 4.1.4 on 2022-12-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_voter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]