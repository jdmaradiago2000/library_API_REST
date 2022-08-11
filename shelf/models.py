from django.db import models

# Createfrom django.db import models
from safedelete.models import SafeDeleteModel

from book_copy.models import BookCopy


# Create your models here.
class Shelf(SafeDeleteModel):
    category = models.CharField(null=False, max_length=12)
    section = models.CharField(null=False, max_length=10)

    def __str__(self):
        return f"{self.section}:::::{self.category} "


class ShelfBookCopy(SafeDeleteModel):
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, unique=True)
    sub_section = models.CharField(max_length=10)

    def __str__(self):
        return f"section {self.shelf.section}==={self.book_copy.book.title}"
