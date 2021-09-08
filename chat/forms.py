# from allauth.account.forms import SignupForm
# from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()


class CustomSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('age',)




