from .models import *


class LibraryService:
    @staticmethod
    def get_total_available_books():
        total_books = libraryBook.objects.count()
        available_books = libraryBook.objects.filter(availability_status=True).count()
        data = {"total_book": total_books, "available_books": available_books}
        return data

    @staticmethod
    def get_total_overdue_books():
        borrowed_books_count = Borrowing.objects.count()
        borrowed_books = Borrowing.objects.filter(due_date__lt=date.today()).count()
        data = {"borrowed_books": borrowed_books_count, "over_due": borrowed_books}
        return data

    @staticmethod
    def get_recently_added_books():
        recently_added_books = libraryBook.objects.order_by("-created_on")[:5]

        return recently_added_books
