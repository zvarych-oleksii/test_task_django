"""Models for the email_validation app."""
from django.db import models


class EmailVerification(models.Model):
    """Model representing email verification status."""

    email = models.EmailField(unique=True)
    is_valid = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Return a string representation of the EmailVerification instance."""
        return self.email
