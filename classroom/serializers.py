from rest_framework import serializers

from .models import *


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['channels'] = ChannelSerializer(instance.channels, many=True).data
        return ret


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['user'] = instance.user.id
        ret['avatar'] = 'https://static.vecteezy.com/system/resources/previews/024/983/914/non_2x/simple-user-default-icon-free-png.png'
        return ret
