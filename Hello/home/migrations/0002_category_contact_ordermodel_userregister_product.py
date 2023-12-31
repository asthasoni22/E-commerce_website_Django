# Generated by Django 4.2.1 on 2023-06-22 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categotyname', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ordermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateTimeField(auto_created=True, auto_now=True)),
                ('productid', models.CharField(max_length=200)),
                ('productqty', models.CharField(max_length=200)),
                ('userId', models.CharField(max_length=200)),
                ('userName', models.CharField(max_length=200)),
                ('userEmail', models.EmailField(max_length=254)),
                ('userContact', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('orderAmount', models.IntegerField()),
                ('paymentMethod', models.CharField(max_length=200)),
                ('transactionId', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='product')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
