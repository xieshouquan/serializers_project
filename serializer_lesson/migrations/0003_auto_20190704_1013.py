# Generated by Django 2.2 on 2019-07-04 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serializer_lesson', '0002_auto_20190704_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='telehpone',
            new_name='telephone',
        ),
    ]
