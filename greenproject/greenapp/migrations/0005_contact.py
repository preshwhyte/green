# Generated by Django 4.0.6 on 2024-03-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenapp', '0004_subscribedusers_alter_news_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
