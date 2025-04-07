from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import	User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    telefone = request.data.get('telefone')

    if not username or not senha:
        return Response({'Erro' : f'Campos incompletos'}, status= status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username).exists():
        return Response({'Erro': f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(
        username = username, 
        password = senha,
        telefone = telefone
    )
    return Response({'Mensagem': f'Usuário {username} criado com sucesso'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logar_usuario(request):
    return Response({"Mensagem":"Olá, Usuário!"}, status=status.HTTP_200_OK)