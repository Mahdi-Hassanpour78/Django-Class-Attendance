from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = get_user_model().objects.create_user(**validated_data)
            return user