from accounts.models import Token, User

class PasswordlessAuthenticationBackend(object):
    def authenticate(self, uid):
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email_id):
        try:
            return User.objects.get(email=email_id)
        except User.DoesNotExist:
            return None
