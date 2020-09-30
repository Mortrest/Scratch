# Generated by Django 3.1.1 on 2020-09-30 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200930_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('datePublished', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.userclass')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.question')),
            ],
        ),
    ]
