from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at')
    # def create(self, validated_data):
    #     return CarModel.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     for k, v in validated_data.items():
    #         setattr(instance, k, v)
    #
    #     instance.save()
    #     return instance
