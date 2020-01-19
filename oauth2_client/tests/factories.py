"""
Test factories for the application models.
"""
# pylint: disable=old-style-class
import random

from factory.django import DjangoModelFactory
from faker import Factory

faker = Factory.create()


def fake_client_id():
    """
    Length and form are not standardized by RFC
    """
    return faker.pystr(min_chars=10, max_chars=100)


def fake_client_secret():
    """
    Length and form are not standardized by RFC
    """
    return faker.pystr(min_chars=10, max_chars=100)


def fake_app_name():
    """
    Get a random app name
    """
    return 'test_app_{}'.format(random.randint(0, 10000))


def fake_token():
    """
    Get fake token string.
    """
    return faker.pystr(min_chars=10, max_chars=20)


class ApplicationFactory(DjangoModelFactory):
    """
    Test factory for Application model.
    """
    class Meta:
        model = 'oauth2_client.Application'

    client_id = fake_client_id()
    client_secret = fake_client_secret()
    name = fake_app_name()


class AccessTokenFactory(DjangoModelFactory):
    """
    Test factory for AccessToken model.
    """
    class Meta:
        model = 'oauth2_client.AccessToken'

    token_type = "Bearer"
    token = fake_token()
