# Generated by Django 4.2.1 on 2023-06-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_post_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imgUrl',
            field=models.ImageField(blank=True, default='blogapp/static/images/blog-2-1000x600.jpg', upload_to='blogapp/static/images'),
        ),
    ]
