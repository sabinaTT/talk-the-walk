# Generated by Django 4.0.4 on 2022-05-15 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_question_the_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='the_question',
            field=models.CharField(max_length=100, verbose_name='Question'),
        ),
    ]