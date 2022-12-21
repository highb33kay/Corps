from webpages.models import CompanyProfile
from django import forms


class CompaniesForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = "__all__"


# class CompanyModelForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=50, required=True)

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name',)
