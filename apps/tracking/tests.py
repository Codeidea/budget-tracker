from django.contrib.auth import login
from django.test import TestCase
from rest_framework.test import APITestCase
from model_mommy import mommy
from apps.users.models import User
from .models import LogCategory, BudgetLog


class AuthenticatedUserMixin():

    def login_user(self, client):
        self.username = 'example@domain.com'
        self.password = 'password'

        self.user = User.objects.create_user(email=self.username, password=self.password)
        client.login(username=self.username, password=self.password)

    def get_user(self):
        return self.user


class LogCategoryTest(APITestCase, AuthenticatedUserMixin):

    def setUp(self):
        self.login_user(self.client)

    def test_fetching_categories(self):
        categories = mommy.make(LogCategory, _quantity=5)
        response = self.client.get('/log_categories', format='json')
        self.assertEqual(len(response.data), len(categories))


class LogEntriesListApiTest(APITestCase, AuthenticatedUserMixin):

    def setUp(self):
        self.login_user(self.client)

    def test_fetching_log_entries(self):
        logs = mommy.make(BudgetLog, _quantity=5)
        response = self.client.get('/logs', format='json')
        self.assertEqual(len(response.data), len(logs))

    def test_filtering_by_date(self):
        mommy.make(BudgetLog, date='2014-02-02')
        mommy.make(BudgetLog, date='2014-07-07')

        response = self.client.get('/logs?date__gt=2014-01-01&date__gt=2014-05-01')
        self.assertEqual(len(response.data), 1)


class CreatingLogTest(APITestCase, AuthenticatedUserMixin):

    def setUp(self):
        self.login_user(self.client)

    def test_validation(self):
        data = {
            'title': 'all',
            'amount': 'wrong',
            'date': '2015-01-01 22:00:00'
        }

        response = self.client.post('/tracking', data)
        self.assertIn('amount', response.data)
        self.assertIn('date', response.data)
        self.assertIn('category', response.data)

    def test_creating_new_log(self):
        category = mommy.make(LogCategory)

        data = {
            'category': category.id,
            'title': 'My expense',
            'amount': '500.50',
            'date': '2015-01-01'
        }

        response = self.client.post('/tracking', data)
        self.assertIn('id', response.data)