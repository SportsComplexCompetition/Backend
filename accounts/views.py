from django.shortcuts import render
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from accounts.serializers import CustomRegisterSeriializer, UserListSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from accounts.models import User
from django.http import JsonResponse

class CustomLoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        mydata = {"pk" : self.user.pk, "email": self.user.email}
        response.data.update(mydata)
        return response

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSeriializer

class UserListViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserJoinCompetitionView(APIView):
    def get(self, request):
        user = User.objects.get(id=3)
        data = user.competition_join_people.values()
        return JsonResponse(list(data), safe=False, json_dumps_params={'ensure_ascii': False})

class UserJoinMeetingView(APIView):
     def get(self, request):
        user = User.objects.get(id=3)
        data = user.meeting_host.values()
        return JsonResponse(list(data), safe=False, json_dumps_params={'ensure_ascii': False})
    