# Generated by Django 4.2.6 on 2023-10-30 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_askhr_hr_id_alter_askhr_id_alter_department_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='req_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AlterField(
            model_name='askhr',
            name='id',
            field=models.CharField(default='ef9ee229-9db9-4fce-97bb-09eb827a16b1', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='c0f2c13a-c88b-4411-a70d-5e79bcd42a99', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(default='b849d8ad-14b7-448e-88b9-84e6085c589c', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.CharField(default='6ce0bcd1-6b3d-489b-ae33-42fe0ec5607b', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default='2df1f577-e1dc-4d82-8390-945edf02a81d', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]
