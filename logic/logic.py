# Checking availability based on check-in and check-out
from datetime import date

class BookingCreateView(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            check_in = serializer.validated_data['check_in']
            check_out = serializer.validated_data['check_out']

            # Check if the room or resort is available for the specified dates
            overlapping_bookings = Booking.objects.filter(
                (Q(room__isnull=False) | Q(resort__isnull=False)) &
                Q(check_in__lt=check_out, check_out__gt=check_in)
            )
            if overlapping_bookings.exists():
                return Response(
                    {'message': 'This room or resort is not available for the selected dates.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Seat availability
class BookingCreateView(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            flight_id = request.data.get('flight')
            seat_number = request.data.get('seat_number')

            # Check if the seat is available on the given flight
            if flight_id and seat_number:
                try:
                    flight = Flight.objects.get(id=flight_id)
                    if seat_number in flight.bookings.values_list('seat_number', flat=True):
                        return Response({'message': 'This seat is already booked.'},
                                        status=status.HTTP_400_BAD_REQUEST)
                except Flight.DoesNotExist:
                    return Response({'message': 'Invalid flight ID.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


