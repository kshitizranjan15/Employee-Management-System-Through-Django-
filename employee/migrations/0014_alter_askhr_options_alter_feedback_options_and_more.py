# Generated by Django 4.2.6 on 2023-10-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_leaverequest_req_to_alter_askhr_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='askhr',
            options={'verbose_name_plural': 'AskHR'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'Feedback'},
        ),
        migrations.AlterModelOptions(
            name='leaverequest',
            options={'verbose_name_plural': 'LeaveRequest'},
        ),
        migrations.AlterField(
            model_name='askhr',
            name='id',
            field=models.CharField(default='135693ae-bd1e-4818-bab0-1668faef078d', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='fdad3196-3609-4bdf-83dd-2515fe90aae0', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='95612469-f690-4362-853e-af8113c0bb50', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.CharField(default='ed803e27-0fcb-452c-bf07-826dd2ad22f7', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default='a2dcec8c-ce04-445e-a5dc-cd14fc1ea787', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]