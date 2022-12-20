# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# # Create your forms here.

# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user


# class UserCreationForm(forms.ModelForm):
    

#     class Meta:
#         model = YourUserModel
#         fields = ('email', 'username')

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)

#         default_password = somefuntion() #Generate the default password

#         user.set_password(default_password ) #Set de default password
#         if commit:
#             user.save()
#         return user