# Generated by Django 4.0.4 on 2022-05-12 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_question_stack_stack_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stack',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='stack',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.stack'),
            preserve_default=False,
        ),
    ]
