from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime

@api_view(['POST'])
def login(request):
    """
    Endpoint for user login.

    This view receives a POST request with user credentials (email and password).
    It checks if the provided credentials are valid and returns a token if authentication is successful.

    Args:
        request (HttpRequest): The incoming HTTP request object containing user credentials.

    Returns:
        Response: JSON response with authentication token and user details if authentication is successful,
                  or an error message with HTTP status code if authentication fails.
    """
    # Check if email or password is missing
    if 'email' not in request.data or request.data['email'] == "":
        return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
    if 'password' not in request.data or request.data['password'] == "":
        return Response({"error": "Password is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    user = get_object_or_404(User, email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found!"}, status=status.HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    # Create a response with the token and user details
    response = Response({
        "token": token.key,
        "user": serializer.data
    })

    # Set a cookie with the token
    cookie_expires = datetime.datetime.now() + datetime.timedelta(days=1)  # expires after 1 day
    response.set_cookie(
        key='auth_token',
        value=token.key,
        expires=cookie_expires,
        httponly=True,  
        secure = False,  # if HTTPS -> True
        samesite='Strict' # Strict, Lax, None
    )
    return response

@api_view(['POST'])
def signup(request):
    """
    Endpoint for user registration.

    This view receives a POST request with user details (username, email, and password).
    It checks if the provided email is already in use, and if not, registers the user and returns a token.

    Args:
        request (HttpRequest): The incoming HTTP request object containing user details.

    Returns:
        Response: JSON response with authentication token and user details if registration is successful,
                  or an error message with HTTP status code if registration fails.
    """    
    # Check if email is already in use
    if User.objects.filter(email=request.data['email']).exists():
        return Response({"error": "This email address is already in use."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])

        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    # Return error if serializer data is not valid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    """
    Endpoint for user logout.

    This view receives a POST request to log out the user.
    It clears the authentication token cookie to log the user out.

    Args:
        request (HttpRequest): The incoming HTTP request object.

    Returns:
        Response: JSON response with a success message indicating successful logout.
    """
    response = Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
    
    # Clear the cookie
    response.delete_cookie('auth_token')
    
    return response

@api_view(['POST'])
def verify_token(request):
    """
    Endpoint for verifying user token.

    This view receives a POST request with a user token.
    It checks if the provided token is valid and returns a success message if it is.

    Args:
        request (HttpRequest): The incoming HTTP request object containing user token.

    Returns:
        Response: JSON response with a success message indicating successful token verification,
                  or an error message with HTTP status code if token is invalid.

    """
    data = request.data
    token = data.get('token')
    if token is None:
        return Response({"error": "No token provided."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        print('Trying to get token')
        token = Token.objects.get(key=token)
        print('Got token', token)
    except Token.DoesNotExist:
        return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Token is valid."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    """
    Test endpoint for token authentication.

    This view is protected and requires a valid authentication token to access.
    It returns a simple message confirming successful token-based authentication.

    Args:
        request (HttpRequest): The incoming HTTP request object containing authentication token.

    Returns:
        Response: JSON response with a success message indicating successful token authentication.
    """
    return Response("passed for {}".format(request.user.email))