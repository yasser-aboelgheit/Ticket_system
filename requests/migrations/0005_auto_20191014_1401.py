# Generated by Django 2.2.6 on 2019-10-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_auto_20191013_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('assigned', 'Assigned'), ('not-assigned', 'NotAssigned'), ('closed', 'Closed')], default='not-assigned', max_length=50),
        ),
    ]
