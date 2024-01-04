from django.db import models


class EmailVerificationResult(models.Model):
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=50, default="invalid")

    def __str__(self) -> str:
        return self.email
