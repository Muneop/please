# Generated by Django 2.2 on 2019-04-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=2048)),
            ],
        ),
    ]
