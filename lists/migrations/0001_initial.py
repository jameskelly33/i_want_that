# Generated by Django 4.2.5 on 2023-11-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WishListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('url', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('person', models.CharField(choices=[('james', 'James'), ('orla', 'Orflaith'), ('jack', 'Jack'), ('flat', 'Flat')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Wish List Items',
                'ordering': ('pk',),
            },
        ),
    ]
