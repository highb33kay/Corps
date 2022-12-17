from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage"),
    # handle the user search form
    path("user_search", views.user_search_view, name="user_search"),
    path("/terms", views.TermsView.as_view(), name="terms"),
]
