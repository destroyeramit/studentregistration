# Generated by Django 2.0.6 on 2018-08-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20180821_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_form4',
            name='tenth_marksheet',
            field=models.FileField(blank=True, null=True, upload_to='f1/%Y/%m/%D/'),
        ),
    ]
