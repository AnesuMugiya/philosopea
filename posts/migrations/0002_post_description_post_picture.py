# Generated by Django 4.1.3 on 2022-11-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='No description', max_length=1500),
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='picture/'),
        ),
    ]
