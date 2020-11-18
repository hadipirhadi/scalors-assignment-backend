# Generated by Django 3.1.3 on 2020-11-18 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0003_tbltodo_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_url', models.URLField()),
                ('text', models.TextField()),
                ('delay', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='board',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boards', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tbltodo',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL),
        ),
    ]
