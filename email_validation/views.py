# email_verification_app/views.py

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmailVerificationResult
from .serializers import EmailVerificationResultSerializer


class EmailVerificationView(APIView):
    def get(self, request, email):
        api_key = "96d95ec2ea53efab6eaa859ebfa0d0a25f028a24"
        url = "https://api.hunter.io/v2/email-verifier"
        params = {"email": email, "api_key": api_key}
        response = requests.get(url, params=params)

        result_data = response.json().get("data", {})

        # Create a dictionary with the relevant fields for the serializer
        serializer_data = {
            "email": email,
            "status": result_data.get("status", ""),
            "result": result_data.get("result", ""),
            "score": result_data.get("score", 0),
            # Add other fields according to the Hunter.io API response
        }

        # Save the result to the database
        serializer = EmailVerificationResultSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save()

        return Response(result_data, status=status.HTTP_200_OK)


class EmailVerificationResultListView(APIView):
    def get(self, request):
        results = EmailVerificationResult.objects.all()
        serializer = EmailVerificationResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
