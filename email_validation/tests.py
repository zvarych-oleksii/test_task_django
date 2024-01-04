"""Module for testing email validation functionality."""
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from email_validation.models import EmailVerification


class EmailVerificationTests(APITestCase):
    """Tests for the EmailVerification."""

    def setUp(self):
        """Set up test data for testing."""
        self.user = User.objects.create_user(username='testuser', password=User.objects.make_random_password())
        self.client.login(username='testuser', password=self.user.password)

        self.email = 'test@gmail.com'
        self.verification = EmailVerification.objects.create(email=self.email)

    def test_email_verification(self):
        """Testing email verification."""
        url = reverse('email-verification', args=[self.email])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_email_list(self):
        """Test getting email list."""
        url = reverse('email-verification-results-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_email_detail(self):
        """Test getting email details."""
        url = reverse('email-verification-results-detail', args=[self.verification.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_email_list(self):
        """Test posting email."""
        url = reverse('email-verification-results-list')
        email_data = {'email': 'new@example.com'}
        response = self.client.post(url, email_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EmailVerification.objects.count(), 2)

    def test_delete_email_list(self):
        """Test deleting email."""
        url = reverse('email-verification-results-list')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EmailVerification.objects.count(), 0)
