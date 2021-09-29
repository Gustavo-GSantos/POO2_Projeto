from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

from .models import BaseDeUsuarios


class UserLoginForm(AuthenticationForm):

    usuario = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Usuário', 'id': 'login-usuario'}))
    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Senha', 'id': 'login-senha'}))


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(
        label='Digite seu Usuário', min_length=4, max_length=50, help_text='Obrigatório')
    email = forms.EmailField(max_length=100, help_text='Obrigatório', error_messages={
        'obrigatório': 'Email é um campo obrigatório!'})
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Repetir senha', widget=forms.PasswordInput)

    class Meta:
        model = BaseDeUsuarios
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = BaseDeUsuarios.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Esse usuário já existe!")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['senha'] != cd['senha2']:
            raise forms.ValidationError('As senhas são diferentes!')
        return cd['senha2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if BaseDeUsuarios.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Esse e-mail já foi usado!')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Usuario'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'nome': 'email', 'id': 'id_email'})
        self.fields['senha'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Senha'})
        self.fields['senha2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repita a senha'})


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = BaseDeUsuarios.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Esse e-mail não é válido ou ainda não foi registrado!')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    nova_senha1 = forms.CharField(
        label='Nova senha', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nova senha', 'id': 'form-newpass'}))
    nova_senha2 = forms.CharField(
        label='Repita a senha', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nova senha', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='E-mail (não pode ser alterado)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Usuario', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Usuario', 'id': 'form-usuario', 'readonly': 'readonly'}))

    primeiro_nome = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-sobrenome'}))

    class Meta:
        model = BaseDeUsuarios
        fields = ('email', 'user_name', 'primeiro_nome',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True