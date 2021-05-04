# Generated by Django 3.1.7 on 2021-05-03 23:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255)),
                ('word', models.PositiveSmallIntegerField()),
                ('city_corporation', models.CharField(choices=[('BARISHAL', 'Barishal'), ('CHITTAGONG', 'Chittagong'), ('COMILLA', 'Comilla'), ('DHAKA_NORTH', 'Dhaka North'), ('DHAKA_SOUTH', 'Dhaka South'), ('GAZIPUR', 'Gazipur'), ('NARAYANGANJ', 'Narayanganj'), ('KHULNA', 'Khulna'), ('MYMENSINGH', 'Mymensingh'), ('RAJSHAHI', 'Rajshahi'), ('RANGPUR', 'Rangpur'), ('SYLHET', 'Sylhet')], max_length=60)),
                ('slug', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('word', 'city_corporation')},
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('TEXT', 'Text'), ('RICH_TEXT', 'Rich Text'), ('NUMBER', 'Number'), ('BOOLEAN', 'Boolean'), ('DATE', 'Date'), ('URL', 'Url'), ('PHONE', 'Phone Number')], default='TEXT', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('path', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Must be a valid phone number of bangladesh', regex='^(?:\\+88|88)?(0(1|9)[3-9]\\d{7,10})$')])),
                ('is_reviewed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='services', to='service.address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='services', to='service.category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_created', to=settings.AUTH_USER_MODEL)),
                ('fields', models.ManyToManyField(blank=True, related_name='_service_fields_+', to='service.Field')),
                ('images', models.ManyToManyField(blank=True, related_name='_service_images_+', to='service.Image')),
                ('reviewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_reviewed', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='service_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='field',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='service.fieldname'),
        ),
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('banner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='service.image')),
            ],
            options={
                'verbose_name_plural': 'Category Types',
            },
        ),
        migrations.CreateModel(
            name='CategoryFieldName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_required', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.category')),
                ('field_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.fieldname')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='banner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='service.image'),
        ),
        migrations.AddField(
            model_name='category',
            name='fields',
            field=models.ManyToManyField(blank=True, related_name='_category_fields_+', through='service.CategoryFieldName', to='service.FieldName'),
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='service.categorytype'),
        ),
    ]