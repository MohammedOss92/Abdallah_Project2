from rest_framework import serializers
from Msgs_Api.models import * 

class MsgsTypesSerializer (serializers.ModelSerializer):
    class Meta:
        model = MsgsTypes
        fields = '__all__'

class MsgsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Msgs
        fields = '__all__'

class MessegasSerializer (serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'