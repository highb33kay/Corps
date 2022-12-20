from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/profile", views.UserProfileView.as_view(), name="profile"),
    path("accounts/status", views.UserStatusView.as_view(), name="status"),
]
