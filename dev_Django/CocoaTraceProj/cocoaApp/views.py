# views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, CustomLoginForm
from rest_framework.views import APIView
from rest_framework.response import Response
from cocoaApp.serializer import *
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from cocoaApp.models import Cooperative

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # user = authenticate(username=username, password=password)
        user = User.objects.get(username=username, password=password)
        if user is not None:
            cooperative = Cooperative.objects.filter(nom=username)[0]
            print(f"====[{cooperative}]")
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username, 'cooperative_id':cooperative.id, 'nom_cooperative':cooperative.nom}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class SacViewSet(viewsets.ModelViewSet):
    queryset = Sac.objects.all()
    serializer_class = SacSerializer

class LotViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    
    

# @ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

# @csrf_exempt  # Désactive le CSRF pour la connexion, à utiliser uniquement en développement.
# def login_view(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)  # Charge les données envoyées en JSON
#             username = data.get("username")
#             password = data.get("password")
#             user_test = User
#             print(f"{username}, == { password}")
#             # Authentifier l'utilisateur
#             # user = authenticate(username=username, password=password)
#             user = User.objects.get(username=username, password=password)
#             print(f"====({user})")
#             if user:  # Si l'utilisateur est trouvé, connectez-le
#                 login(request, user)
#                 return JsonResponse({"message": "Connexion réussie"}, status=200)

#             return JsonResponse({"error": "Identifiants invalides"}, status=400)

#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Erreur dans le format de la requête"}, status=400)

#     return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            role = data.get("role")

            # Authentifier l'utilisateur
            # user = authenticate(username=username, password=password)
            user = User.objects.get(username=username, password=password)
            
            if user:  # Si l'utilisateur est trouvé, connectez-le
                login(request, user)
                id = Cooperative.objects.filter(nom=username)[0].id
                return JsonResponse({
                    "message": "Connexion réussie",
                    "user_id": user.id,
                    "id":id,# Retourne l'ID utilisateur
                    "username": user.username
                }, status=200)

            return JsonResponse({"error": "Identifiants invalides"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Erreur dans le format de la requête"}, status=400)

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Déconnexion réussie"}, status=200)

def check_authentication(request):
    if request.user.is_authenticated:
        return JsonResponse({"isAuthenticated": True, "username": request.user.username, "id": request.user.id})
    return JsonResponse({"isAuthenticated": False})