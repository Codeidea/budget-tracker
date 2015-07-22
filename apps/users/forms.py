# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    email = forms.EmailField(
        max_length=40,
        required=False,
        widget=forms.EmailInput(attrs={'class': 'span3', 'placeholder': 'Adres e-mail'})
    )
    password = forms.CharField(
        label=_("Password"),
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'span3', 'placeholder': 'Hasło'})
    )

    error_messages = {
        'invalid_login': _(u"Wprowadź poprawny email oraz hasło. "
                           u"Uwaga: wielkość liter ma znaczenie!"),
        'inactive': _("To konto jest niekatywne."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        self.user_cache = authenticate(email=email,
                                       password=password)
        if self.user_cache is None:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login'
            )
        else:
            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache