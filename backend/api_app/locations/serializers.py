from rest_framework import serializers as rfs

class LocationSerializer(rfs.Serializer):
    # Would help if we eventually figure out
    # the restrictions lattitudes and longitudes have.
    lat = rfs.FloatField()
    long = rfs.FloatField()
