from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from abstract.permissions import IsOwner
from .serializers import ProfileSerializer
from .models import *


class ProfileDisplay(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        username = self.kwargs['user']
        return Profile.objects.filter(Profile__user__username=username).get(,
