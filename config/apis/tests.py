from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book

class APItests(APITestCase):
    @classmethod

    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='The Great Gatsby', 
            author='F. Scott Fitzgerald', 
            subtitle='Gatsby the Greatest', 
            isbn='978-3-16-148410-0',
            )
        
    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)