from django.urls import path
from .views import EmailVerificationView, EmailVerificationResultListView

urlpatterns = [
    path('verify-email/<str:email>/', EmailVerificationView.as_view(), name='verify-email'),
    path('verification-results/', EmailVerificationResultListView.as_view(), name='verification-results'),
]