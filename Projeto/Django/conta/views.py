from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from pedidos.views import usuario_pedidos

from .forms import RegistrationForm, UserEditForm
from .models import BaseDeUsuarios
from .tokens import token_ativacao_conta


@login_required
def dashboard(request):
    pedidos = usuario_pedidos(request)
    return render(request, 'conta/usuario/dashboard.html', {'section': 'perfil', 'pedidos': pedidos})

@login_required
def editar_detalhes(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, 'conta/usuario/editar_detalhes.html', {'user_form': user_form})

@login_required
def deletar_usuario(request):
    usuario = BaseDeUsuarios.objects.get(user_name=request.user)
    usuario.is_active = False
    usuario.save()
    logout(request)
    return redirect('conta:confirmacao_deletar')

def registrar_conta(request):
    if request.user.is_authenticated:
        return redirect('conta:dashboard')
    
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            usuario = registerForm.save(commit=False)
            usuario.email = registerForm.cleaned_data['email']
            usuario.set_password(registerForm.cleaned_data['senha'])
            usuario.is_active = False
            usuario.save()
            current_site = get_current_site(request)
            assunto = 'Ative sua Conta - Gerenciador de Máscaras'
            mensagem = render_to_string('conta/registro/email_ativacao_conta.html', {
                'usuario': usuario,
                'dominio': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(usuario.pk)),
                'token': token_ativacao_conta.make_token(usuario),
            })
            usuario.email_usuario(assunto=assunto, mensagem=mensagem)
            return HttpResponse('Registrado com sucesso, email para ativação enviado!')
    else:
        registerForm = RegistrationForm()
    return render(request, 'conta/registro/registrar.html', {'form': registerForm})


def ativacao_conta(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        usuario = BaseDeUsuarios.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        usuario = None
    if usuario is not None and token_ativacao_conta.check_token(usuario, token):
        usuario.is_active = True
        usuario.save()
        login(request, usuario)
        return redirect('conta:dashboard')
    else:
        return render(request, 'conta/registro/ativacao_invalida.html')
