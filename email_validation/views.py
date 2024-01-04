from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmailVerification
from .serializers import EmailVerificationSerializer
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

        serializer = EmailVerificationSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save()

        return Response(result_data, status=status.HTTP_200_OK)


class EmailVerificationResultListView(APIView):

    def get(self, request):
        results = EmailVerification.objects.all()
        serializer = EmailVerificationSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        EmailVerification.objects.all().delete()
        return Response("{message: 'Email verification deleted'}", status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailVerificationResultDetailView(RetrieveUpdateDestroyAPIView):
    queryset = EmailVerification.objects.all()
    serializer_class = EmailVerificationSerializer
