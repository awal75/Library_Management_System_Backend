from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.

class Author(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,related_name='author',on_delete=models.CASCADE)
    biography=models.TextField()

    def __str__(self):
        return f'author-{self.user.first_name}'
    
class Member(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,related_name='member',on_delete=models.CASCADE)
    membership_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'member-{self.user.first_name}'

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    ISBN = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=150)

    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    availability_status = models.BooleanField(default=True)

    def clean(self):
        if self.available_copies > self.total_copies:
            raise ValidationError("Available copies cannot exceed total copies")

    def save(self, *args, **kwargs):
        self.availability_status = self.available_copies > 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




class BorrowRecord(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrowrecords')
    member=models.ForeignKey(Member,on_delete=models.CASCADE,related_name='borrowrecords')
    borrow_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField()
    return_status = models.BooleanField(default=False)
    actual_return_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f'Borrow Record-{self.member.user.first_name}'