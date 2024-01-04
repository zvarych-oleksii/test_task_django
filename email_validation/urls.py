from django.urls import path
from .views import EmailVerificationView, EmailVerificationResultListView, EmailVerificationResultDetailView

urlpatterns = [
    path('email-verification/<str:email>/', EmailVerificationView.as_view(), name='email-verification'),
    path('email-verification-results/', EmailVerificationResultListView.as_view(), name='email-verification-results-list'),
    path('email-verification-results/<int:pk>/', EmailVerificationResultDetailView.as_view(), name='email-verification-results-detail'),
]