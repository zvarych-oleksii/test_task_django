"""
Module: email_validation.admin.

Description: Define the admin configuration for the email_validation app.
"""
from django.contrib import admin

from email_validation.models import EmailVerification

admin.site.register(EmailVerification)
