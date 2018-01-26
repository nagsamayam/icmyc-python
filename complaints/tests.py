from django.test import TestCase
from .models import Complaint
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import HttpResponse

User = get_user_model()

class ComplaintModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('admin', 'nag.samayam@gmail.com', '123456')
        Complaint.objects.create(title='Test title1', body='Test description1', user_id=user.id)

    def test_content_context(self):
        complaint = Complaint.objects.first()
        expected_object_title = f'{complaint.title}'
        expected_object_body = f'{complaint.body}'
        self.assertEquals(expected_object_title, 'Test title1')
        self.assertEquals(expected_object_body, 'Test description1')


class ComplaintListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('admin', 'nag.samayam@gmail.com', '123456')
        Complaint.objects.create(title='This is another title', body='This is anohter description', user_id=user.id)

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/complaints/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('complaint-list'))
        self.assertEquals(response.status_code, 200)

    def test_view_users_correct_template(self):
        response = self.client.get(reverse('complaint-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'complaints/index.html')


class ComplaintDetailViewList(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('admin', 'nag.samayam@gmail.com', '123456')
        Complaint.objects.create(title='This is detail title', body='This is detail description', user_id=user.id, slug='this-is-detail-title')
    

    def test_view_url_exists_at_proper_location(self):
        complaint = Complaint.objects.first()
        response = self.client.get(complaint.get_absolute_url())
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        complaint = Complaint.objects.first()
        response = self.client.get(reverse('complaint-detail', kwargs={'slug': complaint.slug}))
        self.assertEquals(response.status_code, 200)

    def test_view_users_correct_template(self):
        complaint = Complaint.objects.first()
        response = self.client.get(reverse('complaint-detail', kwargs={'slug': complaint.slug}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'complaints/detail.html')



