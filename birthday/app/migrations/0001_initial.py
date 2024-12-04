# Generated by Django 5.1.3 on 2024-12-04 04:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('companions', models.CharField(max_length=200)),
                ('attendance', models.CharField(choices=[('assist', 'Asistiré'), ('not_attend', 'No asistiré'), ('maybe', 'Tal vez')], default='assist', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guest', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Invitado',
                'verbose_name_plural': 'Invitados',
                'ordering': ['-id'],
            },
        ),
    ]
