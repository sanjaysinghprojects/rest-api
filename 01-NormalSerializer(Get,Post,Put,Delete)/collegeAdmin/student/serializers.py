from rest_framework import serializers
from .models import student

class studentserializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=20)
    #id=serializers.IntegerField()

    def create(self, validated_data):
        return student.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.age=validated_data.get("age",instance.age)
        instance.address=validated_data.get("address",instance.address)
        instance.save()
        return instance


