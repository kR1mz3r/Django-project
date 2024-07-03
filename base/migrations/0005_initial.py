# Generated by Django 5.0.4 on 2024-05-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0004_delete_basetask'),
        ('project', '0002_alter_task_files_alter_task_updated_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProjectTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(verbose_name='Название проекта')),
                ('description', models.TextField()),
                ('task', models.ManyToManyField(to='project.task', verbose_name='Список задач')),
            ],
            options={
                'verbose_name': 'Проекты (архив)',
                'verbose_name_plural': 'Проекты (архив)',
            },
        ),
    ]
