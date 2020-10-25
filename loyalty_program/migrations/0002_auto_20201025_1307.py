# Generated by Django 3.1.2 on 2020-10-25 13:07

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loyalty_program', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit',
            old_name='credit',
            new_name='points',
        ),
        migrations.CreateModel(
            name='UserContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]