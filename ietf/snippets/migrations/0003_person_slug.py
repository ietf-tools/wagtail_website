# Generated by Django 4.2.7 on 2023-12-12 18:52

from django.db import migrations, models
from wagtail.coreutils import slugify


def generate_person_slugs(apps, schema_editor):
    Person = apps.get_model("snippets.Person")
    for person in Person.objects.all():
        person.slug = slugify(person.name)
        person.save()


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20200414_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default='', max_length=511, unique=True),
            preserve_default=False,
        ),
        migrations.RunPython(generate_person_slugs, migrations.RunPython.noop),
    ]
