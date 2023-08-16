from rest_framework.generics import get_object_or_404, GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CarModel
from .serializer import CarSerializer
from .filters import car_filtered_queryset


class CarListView(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)

    # def get(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    #     qs = car_filtered_queryset(self.request.query_params)
    #     serializer = self.serializer_class(qs, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    # def get(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     car = get_object_or_404(CarModel, pk)
    #     serializer = CarSerializer(car)
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def put(self, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     car = get_object_or_404(CarModel, pk)
    #     data = self.request.data
    #     serializer = CarSerializer(car, data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def patch(self, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     car = get_object_or_404(CarModel, pk)
    #     data = self.request.data
    #     serializer = CarSerializer(car, data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)

    # def delete(self, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     car = get_object_or_404(CarModel, pk)
    #     car.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
