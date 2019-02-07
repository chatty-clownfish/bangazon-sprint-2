# Generated by Django 2.1.5 on 2019-02-07 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('deletedOn', models.DateField(default=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isCompleted', models.BooleanField(default=False)),
                ('deletedOn', models.DateField(default=None)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('accountNumber', models.IntegerField()),
                ('deletedOn', models.DateField(default=None)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('deletedOn', models.DateField(default=None)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deletedOn', models.DateField(default=None)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('deletedOn', models.DateField(default=None)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.ProductType'),
        ),
        migrations.AddField(
            model_name='order',
            name='paymentType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.PaymentType'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(blank=True, through='website.ProductOrder', to='website.Product'),
        ),
    ]
