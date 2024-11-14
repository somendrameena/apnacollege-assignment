from rest_framework.authtoken.models import Token


def generate_token(user):
    try:
        existing_token = Token.objects.get(user=user)
        return existing_token.key
    except Token.DoesNotExist:
        token = Token.objects.create(user=user)
        return token.key