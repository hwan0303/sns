from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=30, label='이름')
    school = forms.CharField(max_length=30, label='학교')
    interests = forms.CharField(max_length=30, label="관심분야")
    grade = forms.CharField(max_length=30, label="학년")

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.school = self.cleaned_data['school']
        user.interests = self.cleaned_data['interests']
        user.grade = self.cleaned_data['grade']
        user.save()
        return user