# books/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Recipe
from django.utils import timezone

class RecipeViewsTestCase(TestCase):

    def setUp(self):
        # Створимо кілька рецептів для тестування
        self.recipe1 = Recipe.objects.create(
            title='Recipe 1',
            description='Description for Recipe 1',
            date=timezone.datetime(2023, 1, 1)
        )
        self.recipe2 = Recipe.objects.create(
            title='Recipe 2',
            description='Description for Recipe 2',
            date=timezone.datetime(2023, 2, 1)
        )

    def test_main_view(self):
        # Перевірка доступності сторінки
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        # Перевірка наявності рецептів у контексті
        self.assertContains(response, 'Recipe 1')
        self.assertContains(response, 'Recipe 2')

    def test_recipe_detail_view(self):
        # Перевірка доступності сторінки детального перегляду рецепту
        response = self.client.get(reverse('recipe_detail', args=[self.recipe1.id]))
        self.assertEqual(response.status_code, 200)
        # Перевірка наявності деталей рецепту у контексті
        self.assertContains(response, 'Recipe 1')
        self.assertContains(response, 'Description for Recipe 1')
