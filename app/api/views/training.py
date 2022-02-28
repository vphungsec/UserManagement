from app.api.models import *
from app.api.serializers import TrainingSerializer
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.core import serializers
import json


def index(request):
    if 'user_id' in request.session:
        user = UserPermission.objects.get(id=request.session['user_id'])
        if user:
            context = {
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'is_admin': user.is_admin,
                    'employee': user.employee
                },
            }
            return render(request, "app/training.html", context)
    return redirect('login')


def get_by_employee(request):
    if 'user_id' in request.session:
        user = UserPermission.objects.get(id=request.session['user_id'])
        data = Training.objects.filter(employee=user.employee.id)
        data = serializers.serialize('json', list(data))
        data = json.loads(data)
        if data:
            trainings = []
            for i in data:
                training = {
                    'pk': i['pk'],
                    'language': i['fields']['language'],
                    'speaking': i['fields']['speaking'],
                    'listening': i['fields']['listening'],
                    'writing': i['fields']['writing'],
                    'score': i['fields']['score'],
                }
                trainings.append(training)
            if trainings:
                return JsonResponse(data=trainings, safe=False, status=200)
    return JsonResponse(data={'error': 'Bad request'}, safe=False, status=400)

# @api_view(['POST'])
# def post(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         # data.score = (float(data.speaking) + float(data.listening) + float(data.writing))/3
#         print(data)
#         # print(str(data))
#         # serializer = TrainingSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrainingView(APIView):

    def get_object(self, pk):
        try:
            return Training.objects.get(pk=pk)
        except Training.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        training = self.get_object(pk)
        serializer = TrainingSerializer(training)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        training = self.get_object(pk)
        serializer = TrainingSerializer(training, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        training = self.get_object(pk)
        training.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
