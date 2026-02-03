from django.test import TestCase, Client
from django.urls import resolve, reverse

from budget.models import Project, Category, Expense
import json

class TestViews(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name='project1',
            budget=10000
        )
        self.list_url = reverse('list')     
        self.detail_url = reverse('detail', args=[self.project.id])      

    def test_project_get(self): 
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_details_get(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')

