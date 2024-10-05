from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from .models import Video, Tiktoker


class TiktokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiktoker
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
