# Generated by Django 3.1.2 on 2021-01-06 09:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebhookTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_generated', models.DateTimeField()),
                ('date_received', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField(default='')),
                ('request_meta', models.TextField(default='')),
                ('status', models.CharField(choices=[(1, 'Unprocessed'), (2, 'Processed'), (3, 'Error')], default=1, max_length=250)),
            ],
            options={
                'db_table': 'data_gather_webhooktransaction',
            },
        ),
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_processed', models.DateTimeField(default=django.utils.timezone.now)),
                ('agent_id_number', models.CharField(max_length=10)),
                ('webhook_transaction', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='coreapp.webhooktransaction')),
            ],
            options={
                'db_table': 'data_gather_formsubmission',
            },
        ),
        migrations.CreateModel(
            name='ActivityManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_processed', models.DateTimeField(default=django.utils.timezone.now)),
                ('activity', models.CharField(max_length=20)),
                ('id_number', models.CharField(max_length=10)),
                ('agent_id_number', models.CharField(max_length=10)),
                ('webhook_transaction', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='coreapp.webhooktransaction')),
            ],
            options={
                'db_table': 'data_gather_activitymanagement',
            },
        ),
    ]