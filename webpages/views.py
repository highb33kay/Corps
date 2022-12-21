from django.views.generic import TemplateView
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import CompaniesForm

# import messages
from django.contrib import messages

# import the company model
from .models import CompanyProfile

# import urls from user_registration_bs4
from user_registration_bs4 import urls

# from django.contrib.auth import get_user_model

# User = get_user_model()
# Create your views here.


class HomePageView(TemplateView):
    template_name = "webpages/homepage.html"


class TermsView(TemplateView):
    template_name = "webpages/terms.html"


class User_search(forms.Form):
    username = forms.CharField()


# form view to check that a user is in the database
def user_search_view(request):
    query_dict = request.GET
    # access the second value in the query dict
    query = query_dict.get("username")
    try:
        print(query_dict)
        user = User.objects.get(username=query)
        print(user)
    except User.DoesNotExist:
        pass
    # if the user exists, redirect to login
    if user:
        return redirect("account_login")

    # else:
    #     form = User_search()
    # return render(request, "webpages/user_search.html", {"form": form})


# form view that save the company details
def company_create(request):
    if request.method == "POST":
        form = CompaniesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Company successfully created")
            return redirect("homepage")
    else:
        form = CompaniesForm()
    return render(request, "webpages/company_create.html", {"form": form})


# form view that save the company details
