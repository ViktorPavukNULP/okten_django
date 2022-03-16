from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ComputerModel
from .serializers import ComputerSerializer

class ComputerListCreateView(APIView):
    def get(self, *args, **kwargs):
        computers = ComputerModel.objects.all()
        serializer = ComputerSerializer(computers, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        computer = self.request.data
        serializer = ComputerSerializer(data=computer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response('Car with this id does not exists', status.HTTP_404_NOT_FOUND)

        computer = ComputerModel.objects.get(pk=pk)
        serializer = ComputerSerializer(computer)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_computer = self.request.data

        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response('Car with this id does not exists', status.HTTP_404_NOT_FOUND)

        computer = ComputerModel.objects.get(pk=pk)
        serializer = ComputerSerializer(computer, data=new_computer)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response('Car with this id does not exists', status.HTTP_404_NOT_FOUND)

        computer = ComputerModel.objects.get(pk=pk)
        computer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
