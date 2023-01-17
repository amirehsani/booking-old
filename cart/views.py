from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from abstract.permissions import IsOwner
from .serializers import UserCartSerializer
from .models import UserCart


class UserCartDisplay(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]
    serializer_class = UserCartSerializer

    def get_queryset(self):
        username = self.kwargs['user']
        return UserCart.objects.filter(UserCart__user__username=username).get()
