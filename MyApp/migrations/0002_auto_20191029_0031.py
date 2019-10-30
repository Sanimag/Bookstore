# Generated by Django 2.2.6 on 2019-10-28 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=3)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='MyApp.Reader'),
            preserve_default=False,
        ),
    ]