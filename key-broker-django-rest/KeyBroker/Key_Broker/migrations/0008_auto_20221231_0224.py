# Generated by Django 3.2.5 on 2022-12-30 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Key_Broker', '0007_auto_20221231_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('name_of_property', models.CharField(max_length=250)),
                ('name_of_user', models.CharField(max_length=250)),
                ('guid', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('property_size', models.IntegerField()),
                ('catagory', models.CharField(max_length=250)),
                ('Area', models.CharField(max_length=250)),
                ('image1', models.CharField(max_length=500)),
                ('image2', models.CharField(max_length=500)),
                ('image3', models.CharField(max_length=500)),
                ('image4', models.CharField(max_length=500)),
                ('phone_no', models.IntegerField()),
                ('date', models.DateField()),
                ('datail', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='property',
        ),
    ]
