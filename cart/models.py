import uuid
from django.db.models import UniqueConstraint

from reservation.models import *


class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_cart')
    cart_number = models.PositiveIntegerField(editable=False, default=uuid.uuid4)

    hotel_room_reservation = models.ForeignKey(HotelRoomReservation, on_delete=models.DO_NOTHING,
                                               verbose_name='Hotel Room Reservation')
    residential_reservation = models.ForeignKey(ResidentialReservation, on_delete=models.DO_NOTHING,
                                                verbose_name='Residential Reservation')
    flight_ticket_reservation = models.ForeignKey(FlightTicketReservation, on_delete=models.DO_NOTHING,
                                                  verbose_name='Flight Ticket Reservation')

    is_payed = models.BooleanField(default=True, verbose_name='Is payed')

    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'cart_number'], name='unique_user_cart')
        ]
