from django.http.response import Http404
from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import ResgisterUserSerializer


# Create your views here.
class RegisterAccountView(APIView):

    def post(self, request):
        serializer = ResgisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["password"] = make_password(serializer.validated_data["password"])
            user = serializer.save()
            token = serializer.insert_token(user)

            data = {
                "id": serializer.data["id"],
                "username": serializer.data["username"],
                "token": token
            }
            return Response(data)
        return Response(serializer.errors, status=400)