# Generated by Django 3.2.12 on 2022-07-26 15:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_post_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
