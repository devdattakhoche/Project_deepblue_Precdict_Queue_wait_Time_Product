# Generated by Django 3.0.2 on 2020-02-14 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0007_remove_feedback_feedbacks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='E_Date',
        ),
    ]