# Generated by Django 3.1.4 on 2020-12-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201226_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='title',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='notefile',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]