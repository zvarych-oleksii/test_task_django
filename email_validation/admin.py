"""
Module: email_validation.admin.

Description: Define the admin configuration for the email_validation app.
"""
from django.contrib import admin

from email_validation.models import EmailVerification


@admin.site.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    """
    Admin class for EmailVerification model.

    This class defines the display configuration for the EmailVerification model
    in the Django admin interface.
    """

    list_display = ('email', 'timestamp')
