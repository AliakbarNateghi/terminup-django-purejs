# Generated by Django 4.1 on 2022-09-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharitz', '0004_alter_course_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklyschedule',
            old_name='day',
            new_name='day0',
        ),
        migrations.AddField(
            model_name='weeklyschedule',
            name='day1',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
