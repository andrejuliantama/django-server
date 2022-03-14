from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User

from .serializers import AuthUserSerializer, UserSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = AuthUserSerializer
  queryset = get_user_model().objects.all()

class UserViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = UserSerializer
  queryset = User.objects.all()

# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(
#             username=request.POST['username'], password=request.POST['password'])
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect!'})
#     else:
#         return render(request, 'accounts/login.html')


# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#     return redirect('home')
