# Generated by Django 4.1.1 on 2022-10-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharitz', '0003_alter_course_ps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentchoise',
            name='ps',
            field=models.CharField(blank=True, default='ندارد', max_length=256, null=True),
        ),
    ]
