from django.contrib import admin
from library import models
# Register your models here.

admin.site.register([models.Book,models.Author,models.Member,models.BorrowRecord])