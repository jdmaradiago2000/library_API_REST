import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from safedelete.models import SafeDeleteModel

from book.models import Book
from users.models import UserLibrary


# Create your models here.
class BookCopy(SafeDeleteModel):
    uuid = models.UUIDField(default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    userBook = models.ForeignKey(
        UserLibrary, on_delete=models.CASCADE, null=True, blank=True
    )
    is_rent = models.BooleanField(default=False)
    is_reserve = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.book.title + f" --- id {self.id}"


@receiver(post_save, sender=BookCopy)
def update_avalible(sender, instance, **kwargs):
    if not kwargs["created"]:
        if instance.is_rent:
            is_available = False
        else:
            is_available = True

        BookCopy.objects.filter(pk=instance.id).update(is_available=is_available)
