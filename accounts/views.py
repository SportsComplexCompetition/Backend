from django.shortcuts import render
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from accounts.serializers import CustomRegisterSeriializer, UserListSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from accounts.models import User
from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAdminUser 
from .persmissions import IsAdminOrIsUserSelf
from rest_framework.exceptions import MethodNotAllowed

class CustomLoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        mydata = {"pk" : self.user.pk, "email": self.user.email}
        response.data.update(mydata)
        return response

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSeriializer

class UserListViewSet(ModelViewSet):
    permission_classes = (IsAdminOrIsUserSelf, )
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    http_method_names = ['get']
    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")

class UserJoinCompetitionView(APIView):
    permission_classes = (IsAdminOrIsUserSelf, )
    def get(self, request):
        user = User.objects.get(id=request.user.pk)
        data = user.competition_join_people.values()
        return JsonResponse(list(data), safe=False, json_dumps_params={'ensure_ascii': False})

class UserJoinMeetingView(APIView):
    permission_classes = (IsAdminOrIsUserSelf, )
    def get(self, request):
        user = User.objects.get(id=request.user.pk)
        data = user.meeting_host.values()
        print(data)
        return JsonResponse(list(data), safe=False, json_dumps_params={'ensure_ascii': False})
    