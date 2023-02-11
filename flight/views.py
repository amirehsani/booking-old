from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.settings import DEFAULT_CACHE_TTL
from .serializers import *


class FlightDisplay(ListAPIView):
    queryset = Flight.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = FlightSerializer

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 0.2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FlightTicketDisplay(ListAPIView):
    queryset = FlightTicket.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = FlightTicketSerializer

    @method_decorator(cache_page(DEFAULT_CACHE_TTL * 0.2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
