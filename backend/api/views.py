from django.contrib.auth import get_user_model, authenticate

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import UserSerializer
from api.utils import generate_token

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username and password:
        user = authenticate(username=username, password=password)
        if user is not None:
            user_data = UserSerializer(user).data
            user_data['token'] = generate_token(user)
            return Response(user_data)
        else:
            data = {
                "message": "Invalid Credentials"
            }
            return Response(data, status=400)
    else:
        data = {
            "message": "Invalid Input"
        }
        return Response(data, status=400)