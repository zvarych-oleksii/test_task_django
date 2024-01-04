"""Serializers for the email_validation app."""

from rest_framework import serializers

from email_validation.models import EmailVerification


class EmailVerificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the EmailVerification model.

    This serializer is used to convert EmailVerification model instances to JSON
    representations and vice versa.
    """

    class Meta(object):
        """
        Meta class for EmailVerificationSerializer.

        Specifies the model and fields to include in the serialization process.
        """

        model = EmailVerification
        fields = '__all__'
