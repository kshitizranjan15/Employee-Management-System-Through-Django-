# Generated by Django 4.2.6 on 2023-10-28 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_employee_manager_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'Feedbacks'},
        ),
        migrations.AddField(
            model_name='department',
            name='leader_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default='Manager', max_length=80),
        ),
        migrations.AddField(
            model_name='project',
            name='leader_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='annual_leave',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='employee',
            name='casual_leave',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='manager_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sick_leave',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='fed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='given_feedback', to='employee.employee'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='fed_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recieved_feedback', to='employee.employee'),
        ),
    ]
