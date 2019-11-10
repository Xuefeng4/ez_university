# Generated by Django 2.2.5 on 2019-10-27 20:26

from django.db import migrations

SEMESTERS =[
    {
        "semester_name":"2019 - Summer",
    },
    {
        "semester_name":"2019 - Fall",
    },
    {
        "semester_name":"2020 - Spring",
    },
    {
        "semester_name":"2020 - Summer",
    },
    {
        "semester_name":"2020 - Fall",
    },
]

def add_semester_data(apps, schema_editor):
    semester_model_class = apps.get_model('courseinfo','Semester')
    for semester in SEMESTERS:
        semester_object = semester_model_class.objects.create(
            semester_name=semester['semester_name'],
        )
        semester_object.save()

def remove_semester_data(apps, schema_editor):
    semester_model_class = apps.get_model('courseinfo','Semester')
    for semester in SEMESTERS:
        semester_object = semester_model_class.objects.get(
            semester_name=semester['semester_name'],
        )
        semester_object.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0003_auto_20191027_2018'),
    ]

    operations = [
        migrations.RunPython(
            add_semester_data,
            remove_semester_data
        )
    ]
