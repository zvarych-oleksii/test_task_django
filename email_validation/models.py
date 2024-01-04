from django.db import models


class EmailVerificationResult(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email
