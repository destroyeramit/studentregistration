# Generated by Django 2.0.6 on 2018-08-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20180821_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_form4',
            name='tenth_marksheet',
            field=models.FileField(blank=True, null=True, upload_to='user_%d/%Y/%m/%D/'),
        ),
    ]
