import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.core.cache import cache

from .serializers import LocationSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def save_location(request):
    data = request.data
    user = request.user

    serializer = LocationSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    validated_data = serializer.validated_data

    cache.set(
        user.id,
        json.dumps(validated_data),
        timeout=604800 # a week
    )

    return Response(data=validated_data)
