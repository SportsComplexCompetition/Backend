from django.shortcuts import render
from rest_auth.views import LoginView
# from rest_auth.registration.views import RegisterView

class CustomLoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        mydata = {"pk" : self.user.pk, "email": self.user.email}
        response.data.update(mydata)
        return response

# class CustomRegisterView(RegisterView):
#     serializer_class = CustomRegisterSerializer