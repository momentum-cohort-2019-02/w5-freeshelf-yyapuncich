from django.db import models
from django.db.models import DateTimeField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    """Author for the online books"""
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    """Catagories of different online books available"""
    
    category = models.CharField(max_length=100,default=None,)

    def __str__(self):
        return self.category
    
class Book(models.Model):
    """All the books available on the free shelf"""
    # Fields
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    book_url = models.URLField(max_length=200)
    date_added = models.DateField()
    slug = models.SlugField()

    class Meta:
        ordering = ['-date_added']

    # Methods for the model
    def get_short_description(self):
        return f'{{ self.description|truncatewords:15 }}'

    # def get_string_category(self):
    #     """Returns string representation of category for specific book"""
    #     return self.category

    def get_absolute_url(self):
        """Returns the url to access particular instance of Book model"""
        return reverse("book_detail", args=[str(self.id)])
    # From lecture 3-12 on Slugs...
    def set_slug(self):
        """Setting slug field to auto-generate and make unique each time even if title is same title as another book-- it will add int at end if needed"""
        if self.slug:
            return
        base_slug = slugify(self.title)
        # Local variable slug below
        slug = base_slug
        n = 0
        # While the field slug is already in DB and equal to new local slug, run this loop, else return the slug name without an int at end
        while Book.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)

        self.slug = slug

    def save(self, *args, **kwargs):
        """Need to change default save so that slug field is hidden in admin"""
        self.set_slug()
        super().save(*args, **kwargs)
    
    # String representation of model
    def __str__(self):
        return self.title
    
class Favorite(models.Model):
    """Model representing User choices for books they want to read"""

    FAV_STATUS = (
        ('TR', 'To Read'),
        ('RD', 'Reading'),
        ('DN', 'Done Read'),
    )
