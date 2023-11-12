# Generated by Django 4.2.6 on 2023-11-12 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0007_remove_branch_working_employees'),
        ('packages', '0004_package_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='branch',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='branches.branch'),
        ),
    ]
