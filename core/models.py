from django.db import models
from django.db.models import DateTimeField

# Create your models here.
class Author(models.Model):
    """Author for the online books"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Catagory(models.Model):
    """Catagories of different online books available"""
    SCI_FI = 'SCF'
    PROG = 'PRG'
    FEM = 'FEM'
    POL = 'POL'
    HUM = 'HUM'

    CATAGORY_CHOICES = (
        (SCI_FI, 'Science Fiction'),
        (PROG, 'Programming'),
        (FEM, 'Feminism'),
        (POL, 'Politics'),
        (HUM, 'Humor'),
    )
    
    catagory = models.CharField(
        max_length=10,
        choices=CATAGORY_CHOICES,
        default=None,
    )

    def __str__(self):
        return self.catagory
    
class Book(models.Model):
    """All the books available on the free shelf"""
    # Fields
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    catagory = models.ManyToManyField(Catagory)
    description = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    # Methods for the model
    def get_absolute_url(self):
        """Returns the url to access particular instance of Book model"""
        return reverse("book_detail", args=[str(self.id)])
    
    # String representation of model
    def __str__(self):
        return self.title
    