# Generated by Django 3.1.7 on 2022-05-31 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tienda', '0003_sale_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AlterModelOptions(
            name='sale',
            options={'verbose_name': 'Sale', 'verbose_name_plural': 'Sales'},
        ),
        migrations.AddField(
            model_name='sale',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]