# Generated by Django 2.1.7 on 2019-03-12 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='catagory',
            field=models.CharField(choices=[('SCF', 'Science Fiction'), ('PRG', 'Programming'), ('FEM', 'Feminism'), ('POL', 'Politics'), ('HUM', 'Humor')], default=None, max_length=10),
        ),
    ]
