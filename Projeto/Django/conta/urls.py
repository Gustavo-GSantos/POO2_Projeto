from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .forms import (PwdResetConfirmForm, PwdResetForm, UserLoginForm)

app_name = 'conta'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='conta/registro/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/conta/login/'), name='logout'),
    path('registrar/', views.registrar_conta, name='registrar'),
    path('ativar/<slug:uidb64>/<slug:token>)/', views.ativacao_conta, name='ativar'),

    path('resetar_senha/', auth_views.PasswordResetView.as_view(template_name="conta/usuario/resetar_senha_form.html",
                                                                 success_url='email_confirmacao_resetar_senha',
                                                                 email_template_name='conta/usuario/email_resetar_senha.html',
                                                                 form_class=PwdResetForm), name='senhareset'),
    path('confirmar_resetar_senha/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='conta/usuario/confirmar_resetar_senha.html',
                                                                                                success_url='senha_resetada/',
                                                                                                form_class=PwdResetConfirmForm),
         name="confirmar_resetar_senha"),
    path('resetar_senha/email_confirmacao_resetar_senha/',
         TemplateView.as_view(template_name="conta/usuario/reset_status.html"), name='password_reset_done'),
    path('confirmar_resetar_senha/Mg/senha_resetada/',
         TemplateView.as_view(template_name="conta/usuario/reset_status.html"), name='senha_resetada'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil/editar/', views.editar_detalhes, name='editar_detalhes'),
    path('perfil/deletar_usuario/', views.deletar_usuario, name='deletar_usuario'),
    path('perfil/confirmar_delete/', TemplateView.as_view(template_name="conta/usuario/confirmar_delete.html"), name='confirmacao_deletar'),
]