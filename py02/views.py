from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import Event
from .serializers import EventSerializer

class CreateEventView(APIView):
    def post(self, request, *args, **kwargs):
        # Dados do request
        data = request.data
        
        # Validação: end_date deve ser maior ou igual a start_date
        try:
            inicio = data.get('inicio')
            fim = data.get('fim')
            if fim < inicio:
                return Response(
                    {'detail': 'A data de término não pode ser anterior à data de início.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except KeyError:
            return Response(
                {'detail': 'Data de início e data de fim são necessárias.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validação: o nome do evento já existe
        event_name = data.get('name')
        if Event.objects.filter(name=event_name).exists():
            return Response(
                {'detail': 'Evento já existe com esse nome.'},
                status=status.HTTP_409_CONFLICT
            )
        
        # Criar o evento
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Salva o evento no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

