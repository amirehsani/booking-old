from rest_framework.generics import RetrieveUpdateAPIView
from abstract.permissions import IsOwner
from .serializers import UserCartSerializer
from .models import UserCart


class UserCartDisplay(RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    serializer_class = UserCartSerializer

    def get_queryset(self):
        username = self.kwargs['user']
        return UserCart.objects.filter(UserCart__user__username=username).get()
