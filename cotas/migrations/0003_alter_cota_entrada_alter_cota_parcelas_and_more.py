# Generated by Django 4.1 on 2022-08-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotas', '0002_alter_cota_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cota',
            name='entrada',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='cota',
            name='parcelas',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='cota',
            name='segmento',
            field=models.CharField(default=0, max_length=140),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cota',
            name='valor',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='cota',
            name='vencimento',
            field=models.CharField(max_length=140),
        ),
    ]