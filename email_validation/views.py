"""App views for email."""

from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from email_validation.models import EmailVerification
from email_validation.serializers import EmailVerificationSerializer
from email_validation.utils.hunter_validator import hunter_validator


class EmailVerificationView(APIView):
    """Email verification with hunters.io."""

    def get(self, request, email):
        """Verify email."""
        result_data = hunter_validator(email)
        serializer_data = {
            'email': email,
            'is_valid': result_data.get('status', '') == 'valid',
        }

        serializer = EmailVerificationSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save()

        return Response(result_data, status=status.HTTP_200_OK)


class EmailVerificationResultListView(APIView):
    """Email api list endpoints get, post, put, delete."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """List all email verification results."""
        emails_list = EmailVerification.objects.all()
        serializer = EmailVerificationSerializer(emails_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        """Delete email verification."""
        EmailVerification.objects.all().delete()
        return Response({'message': 'Email verification deleted'}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        """Email api list endpoints post."""
        serializer = EmailVerificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailVerificationResultDetailView(RetrieveUpdateDestroyAPIView):
    """Email api detail endpoints get, put, delete."""

    permission_classes = [IsAuthenticated]
    queryset = EmailVerification.objects.all()
    serializer_class = EmailVerificationSerializer
