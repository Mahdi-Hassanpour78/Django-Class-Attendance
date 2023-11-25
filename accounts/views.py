from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializers


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializers

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
