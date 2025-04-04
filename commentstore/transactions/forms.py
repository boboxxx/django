from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from transactions.models import Points, PointsTransfer


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    points = forms.IntegerField(initial=100)

    class Meta:
        model = User
        fields = ("username", "points", "email", "password1", "password2")

    def save(self, *args, **kwargs):
        instance = super(RegisterForm, self).save(*args, **kwargs)
        Points.objects.create(name=instance, points=self.cleaned_data['points'])
        return instance


class PointsTransferForm(forms.ModelForm):
    class Meta:
        model = PointsTransfer
        fields = ['enter_your_username', 'enter_destination_username', 'enter_points_to_transfer']
