# Generated by Django 2.0 on 2018-02-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FRCComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compCode', models.CharField(max_length=30)),
                ('shortName', models.TextField()),
                ('longName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FRCTeam',
            fields=[
                ('key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('nickname', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='frccomp',
            name='teams',
            field=models.ManyToManyField(to='trade.FRCTeam'),
        ),
    ]