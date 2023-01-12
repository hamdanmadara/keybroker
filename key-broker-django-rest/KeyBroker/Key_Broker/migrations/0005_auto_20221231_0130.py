# Generated by Django 3.2.5 on 2022-12-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Key_Broker', '0004_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='interested_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_user', models.CharField(max_length=250)),
                ('property_guid', models.CharField(max_length=250)),
                ('phone_no', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='upload_property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_property', models.CharField(max_length=250)),
                ('name_of_user', models.CharField(max_length=250)),
                ('guid', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('property_size', models.IntegerField()),
                ('catagory', models.CharField(max_length=250)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
                ('image4', models.ImageField(upload_to='')),
                ('phone_no', models.IntegerField()),
                ('date', models.DateField()),
                ('datail', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]