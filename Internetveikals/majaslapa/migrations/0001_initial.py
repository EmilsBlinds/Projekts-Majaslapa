# Generated by Django 4.1.1 on 2022-09-19 14:30

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Request and unique', max_length=255, unique=True, verbose_name='Nepieciešams un unikāls')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Kategorijas drošs URL')),
                ('is_active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='majaslapa.category')),
            ],
            options={
                'verbose_name': 'Kategorija',
                'verbose_name_plural': 'Kategorījas',
            },
        ),
    ]
