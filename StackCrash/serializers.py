from rest_framework import serializers
from StackCrash.models import History


class HistorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField()
    url = serializers.CharField(max_length=2048)
    title = serializers.CharField(max_length=1024)
    time = serializers.FloatField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return History.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.date = validated_data.get('date', instance.date)
        instance.url = validated_data.get('url', instance.url)
        instance.title = validated_data.get('title', instance.title)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance