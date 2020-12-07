from django.shortcuts import render
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from accounts.serializers import CustomRegisterSeriializer, UserListSerializer
from rest_framework.viewsets import ModelViewSet
from accounts.models import User

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

