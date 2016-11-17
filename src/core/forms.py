from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("The username already exists. Please try another one.")

    def clean_email(self):
        email = self.cleaned_data['email']
        user = self.cleaned_data['username']
        if len(email) == 0:  # емайл не указан
            raise forms.ValidationError("Insert the e-mail")
        # проверяем на уникальность
        try:
            u = User.objects.get(email=email)
            if u.id != user.id:  # если принадлежит другому пользователю, то ошибка
                raise forms.ValidationError("This email is already in use")
        except User.DoesNotExist:
            pass
        return email

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields did not match.")
        return self.cleaned_data