from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        # user.username = data['username']
        # user.email = data['email']
        #        user.first_name = data['first_name']
        #        user.last_name = data['last_name']
        # user.sex = data['sex']
        user.age = data['age']
        #        user.city = data['city']
        #        user.country = data['country']
        if 'password1' in data:
            user.set_password(data['password1'])
            user.save()
        else:
            user.set_unusable_password()
            self.populate_username(request, user)
        return user


