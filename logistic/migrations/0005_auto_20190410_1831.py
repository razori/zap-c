# Generated by Django 2.2 on 2019-04-10 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0004_auto_20190410_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daytasks',
            name='get_set',
            field=models.CharField(choices=[('Забрать', 'Забрать'), ('Отдать', 'Отдать'), ('Ничего', 'Ничего')], default='Ничего', help_text='Отдать клиенту, забрать у клиента либо ничего не делать', max_length=7, verbose_name='Отдать\\забрать'),
        ),
    ]