from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.views.generic import View

from . import forms


class CustomPasswordChangeView(PasswordChangeView):
    success_message = "Votre mot de passe a été changé avec succès."

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        errors = form.errors.get('__all__') or form.errors.get('new_password2')
        if errors:
            messages.error(self.request, errors[0])
        return response


def signup_page(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})
