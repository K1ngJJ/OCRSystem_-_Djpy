# Generated by Django 2.1.7 on 2019-02-20 03:26

from django.db import migrations


def create_default_templates(apps, schema_editor):
    MyObject = apps.get_model(
        'OCRSystemApp', 'MyObject')

    objs = [
        MyObject(
            name="OBJ 1",
            limit_quantity=10.7,
            measurement_unit='1'
        ),
        MyObject(
            name="OBJ 2",
            limit_quantity=40.1,
            measurement_unit='2'
        ),
        MyObject(
            name="OBJ 3",
            limit_quantity=107,
            measurement_unit='3'
        ),
        MyObject(
            name="OBJ 4",
            limit_quantity=10.7,
            measurement_unit='4'
        ),
        MyObject(
            name="OBJ 5",
            limit_quantity=10.7,
            measurement_unit='2'
        ),
        MyObject(
            name="OBJ 6",
            limit_quantity=72,
            measurement_unit='1'
        )
    ]
    MyObject.objects.bulk_create(objs)


class Migration(migrations.Migration):

    dependencies = [
        ('OCRSystemApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_templates),
    ]
