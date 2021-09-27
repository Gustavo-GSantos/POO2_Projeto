from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, usuario, timestamp):
        return (
            text_type(usuario.pk) + text_type(timestamp) +
            text_type(usuario.is_active)
        )


token_ativacao_conta = AccountActivationTokenGenerator()