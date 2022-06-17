from rest_framework import serializers
from .models import MobileDeviceModel

class MobileDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MobileDeviceModel # this is the model that is being serialized
        fields = ('mobile_name', 'mobile_price', 'mobile_quantity')

