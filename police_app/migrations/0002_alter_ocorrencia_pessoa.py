# Generated by Django 4.2.4 on 2023-09-02 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('police_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocorrencia',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='police_app.pessoa'),
        ),
    ]
