# Generated by Django 2.1.7 on 2019-03-16 02:07
import os.path, csv
from django.conf import settings
from django.core.files import File
from django.db import migrations
from django.utils.text import slugify

def get_book_csv(apps, schema_editor):
    """Read CSV file with book list of ebooks and insert them into DB"""
    Book = apps.get_model('core', 'Book')
    Author = apps.get_model('core', 'Author')
    Category = apps.get_model('core', 'Category')
    datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    datafile = os.path.join(datapath, 'Freeshelf_CSV_3_15.csv')

    Book.objects.all().delete()
    Category.objects.all().delete()

    with open(datafile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            book_title = row['title']
            # The following ensures we will not create duplicate books
            if Book.objects.filter(title=book_title).count():
                continue
            # get or create
            author, _ = Author.objects.get_or_create(
                name=row['author'],
            )
            author.save()

            category, _ = Category.objects.get_or_create(
                name=row['category'],
            )
            category.save()
            

            book = Book(
                title=row['title'],
                author=author,
                description=row['description'],
                book_url=row['book_url'],
                date_added=row['date_added'],
            )
            # Needed to slugify my title here because I was getting an error:
            # 'django.db.utils.IntegrityError: UNIQUE constraint failed: core_book.slug'
            book.slug = slugify(book.title)[:49]
            book.save()
            book.categories.add(category)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_fixCatagoriesMigrateData'),
    ]

    operations = [
        migrations.RunPython(get_book_csv)
    ]
