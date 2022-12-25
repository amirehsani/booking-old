from rest_framework.generics import RetrieveAPIView
from abstract.permissions import IsOwner
from .serializers import ProfileSerializer
from .models import *


class ProfileDisplay(RetrieveAPIView):
    permission_classes = [IsOwner]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        username = self.kwargs['user']
        return Profile.objects.get(Profile__user__username=username)
