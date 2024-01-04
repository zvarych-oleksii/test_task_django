# email_verification_app/views.py

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmailVerificationResult
from .serializers import EmailVerificationResultSerializer
from .utils.hunter_validator import hunter_validator


class EmailVerificationView(APIView):
    def get(self, request, email):
        result_data = hunter_validator(email)
        serializer_data = {
            "email": email,
            "status": result_data.get("status", ""),
            "result": result_data.get("result", ""),
            "score": result_data.get("score", 0),
        }

        serializer = EmailVerificationResultSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save()

        return Response(result_data, status=status.HTTP_200_OK)


class EmailVerificationResultListView(APIView):
    def get(self, request):
        results = EmailVerificationResult.objects.all()
        serializer = EmailVerificationResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
