from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
                    title='Harry Potter', 
                    author='JK Rowling', 
                    subtitle='Wizarding World',
                    isbn='978-3-16-148410-0',
                    )
        
    def test_book_content(self):
        self.assertEqual(self.book.title, 'Harry Potter')
        self.assertEqual(self.book.author, 'JK Rowling')
        self.assertEqual(self.book.subtitle, 'Wizarding World')
        self.assertEqual(self.book.isbn, '978-3-16-148410-0')


    def test_book_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')