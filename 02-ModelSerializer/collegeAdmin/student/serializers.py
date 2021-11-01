from rest_framework import serializers
from .models import student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        # fields=["name","age","address"]
        fields="__all__"



