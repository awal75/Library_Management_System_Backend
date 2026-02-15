from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=50)
    biography=models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    ISBN=models.CharField(max_length=100)
    category=models.CharField(max_length=150)
    availability_status=models.BooleanField(default=False)


    def __str__(self):
        return self.title
    

class Member(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    membership_date=models.DateTimeField(auto_now_add=True)


class BorrowRecord(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrowrecords')
    member=models.ForeignKey(Member,on_delete=models.CASCADE,related_name='borrowrecords')
    borrow_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField()

    def __str__(self):
        return f'Borrow Record'