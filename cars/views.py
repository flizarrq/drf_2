from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from .models import CarModel
from .serializers import CarSerializer, CarAllSerializer


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(cars, many=True)
        # res = [model_to_dict(car) for car in cars]
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # car = CarModel(**data)
        # car.save()

        # car = CarModel.objects.create(**serializer.data)
        # serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        data: dict = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        # for k, v in data.items():
        #     setattr(car, k, v)
        # car.save()
        serializer = CarSerializer(car, data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        data: dict = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car, data, partial=True)

        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()
        return Response(status=status.HTTP_204_NO_CONTENT)
