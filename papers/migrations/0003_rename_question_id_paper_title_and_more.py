# Generated by Django 4.2.3 on 2023-07-10 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_rename_papers_paper'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='question_id',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='question_type',
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(max_length=100)),
                ('question_text', models.TextField()),
                ('options', models.CharField(max_length=100)),
                ('question_type', models.CharField(max_length=100)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='papers.paper')),
            ],
        ),
    ]