from ast import Pass
from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.authentication import PasswordlessAuthenticationBackend
from accounts.models import Token

User = get_user_model()


class AuthenticateTest(TestCase):
    def test_returns_None_if_no_such_token(self):
        result = PasswordlessAuthenticationBackend().authenticate(
            'no-such-token'
        )
        self.assertIsNone(result)

    def test_returns_new_user_with_correct_email_if_token_exists(self):
        email = "edith@example.com"
        token = Token.objects.create(email=email)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        new_user = User.objects.get(email=email)
        self.assertEqual(user, new_user)

    def test_returns_existing_user_with_correct_email_if_token_exists(self):
        email = "edith@example.com"
        existing_user = User.objects.create(email=email)
        token = Token.objects.create(email=email)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        self.assertEqual(user, existing_user)


class GetUserTest(TestCase):
    def test_get_user_by_email(self):
        email = "edith@example.com"
        User.objects.create(email="another@example.com")
        desired_user = User.objects.create(email=email)
        found_user = PasswordlessAuthenticationBackend().get_user(email)
        self.assertEqual(desired_user, found_user)

    def test_returns_None_if_no_user_with_email(self):
        self.assertIsNone(
            PasswordlessAuthenticationBackend().get_user("edith@example.com")
        )