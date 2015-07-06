from django.test import TransactionTestCase
from django.contrib.auth.models import User
from client_app.models import Client
from models import Project
from views import get_week_month_year


class Project_Test(TransactionTestCase):

    def setUp(self):
        self.user = User.objects.create(username="example", email='hello@world.com', password='example')
        self.client = Client.objects.create(user=self.user, company_info='Test Company Info ...')
        self.user = Project.objects.create(client=self.client, name="Test Project")

    def test_data_available(self):
        client_list = Client.objects.all()
        self.assertEqual(len(client_list), 1)
        project_list = Project.objects.all()
        self.assertEqual(len(project_list), 1)
        new_project_list = get_week_month_year(project_list)
        current_week_project = new_project_list[0]
        current_month_project = new_project_list[1]
        current_year_project = new_project_list[2]
        self.assertEqual(len(current_week_project), 1)
        self.assertEqual(len(current_month_project), 1)
        self.assertEqual(len(current_year_project), 1)