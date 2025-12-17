from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

       
        Menu.objects.create(title="Burger", price="9.99", inventory=10)
        Menu.objects.create(title="Pizza", price="12.50", inventory=5)
        Menu.objects.create(title="Salad", price="7.25", inventory=20)


        self.url = "/restaurant/menu/"

    def test_getall(self):
        response = self.client.get(self.url)

        menus = Menu.objects.all()
        serialized = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)
