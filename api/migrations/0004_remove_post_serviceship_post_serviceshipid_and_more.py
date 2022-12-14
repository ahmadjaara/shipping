# Generated by Django 4.1.2 on 2022-10-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_serviceship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='serviceship',
        ),
        migrations.AddField(
            model_name='post',
            name='serviceShipID',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='height',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='length',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='weight',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='width',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
