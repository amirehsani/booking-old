from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# UserProfile display API
@api_view(['GET'])
@permission_classes(IsAuthenticated)
def user_profile_display(request, username):
    pass
