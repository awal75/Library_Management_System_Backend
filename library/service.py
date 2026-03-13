from django.db import transaction
from library.models import BorrowRecord, Book,Member
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth import get_user_model

User=get_user_model()


class BookService:

    MAX_BORROW_LIMIT = 3

    @staticmethod
    @transaction.atomic
    def borrow_book(book_id, member, return_date):

        book = Book.objects.select_for_update().get(id=book_id)

        if book.available_copies <= 0:
            raise ValidationError({"detail": "No available copies for this book."})

        active_borrows = BorrowRecord.objects.filter(
            member=member,
            return_status=False
        )

        if active_borrows.count() >= BookService.MAX_BORROW_LIMIT: # every user borrow maximum 2 books at a time
            raise ValidationError({
                "detail": "You have reached the maximum borrow limit."
            })

        if active_borrows.filter(book=book).exists():
            raise ValidationError({
                "detail": "You have already borrowed this book."
            })

        borrow = BorrowRecord.objects.create(
            member=member,
            book=book,
            return_date=return_date
        )

        book.available_copies -= 1
        book.save(update_fields=["available_copies"])

        return borrow
    
    @staticmethod
    @transaction.atomic
    def return_book(book_id,email):
        book=book = Book.objects.select_for_update().get(id=book_id)
        user=get_object_or_404(User,email=email)
        member=user.member

        borrowed=BorrowRecord.objects.filter(book=book,member=member,return_status=False).first()

        if not borrowed:
            raise ValidationError({"detail": "No active borrow record found"})
        book.available_copies+=1
        book.save()
        borrowed.actual_return_date=timezone.now()
        borrowed.return_status=True
        borrowed.save()
        return borrowed
        