from django.db import models
from safedelete.models import SafeDeleteModel


# Create your models here.
class Category(SafeDeleteModel):
    name = models.CharField(max_length=150)
    category_status = [
        ("active", "active"),
        ("inactive", "inactive"),
    ]
    status = models.CharField(max_length=15, choices=category_status, default="active")

    def __str__(self):
        return self.name


class Author(SafeDeleteModel):
    full_name = models.CharField(max_length=150)
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class Book(SafeDeleteModel):
    title = models.CharField(max_length=100, null=False)
    topic = models.CharField(
        max_length=100,
    )
    book_status = [
        ("avalible", "avalible"),
        ("reserved", "reserved"),
    ]
    status = models.CharField(max_length=15, choices=book_status, default="avalible")
    isbn = models.CharField("ISBN", max_length=13, help_text="13")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def full_name(self):
        return self.Author.get_full_name()

    def __str__(self):
        return self.title
