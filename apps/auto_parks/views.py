from django.http import Http404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,CreateModelMixin

from .models import AutoParkModel
from .serializer import AutoParkSerializer
from apps.cars.serializer import CarSerializer
from apps.cars.models import CarModel


class AutoParkListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    #     qs = AutoParkModel.objects.all()
    #     serializer = AutoParkSerializer(qs, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = AutoParkSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)


class AutoParkCarListCreateView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        exists = AutoParkModel.objects.filter(pk=pk).exists()
        if not exists:
            raise Http404()
        cars = CarModel.objects.filter(auto_park_id=pk)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        exists = AutoParkModel.objects.filter(pk=pk).exists()
        if not exists:
            raise Http404()
        serializer.save(auto_park_id=pk)
        return Response(serializer.data, status.HTTP_201_CREATED)
