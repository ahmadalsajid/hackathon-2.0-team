from django.shortcuts import get_object_or_404
from django.db import IntegrityError, transaction
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from users.serializers import VideoSerializer, TiktokerSerializer
from users.models import Video, Tiktoker
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render


class VideoViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny, ]
    """
        Parameters: items_per_page=10, page=1, username=some_user
        """

    def list(self, request):
        query_params = request.query_params.dict()
        items_per_page = int(query_params.get('items_per_page', '10'))
        page = int(query_params.get('page', '1'))
        _start_index = (page - 1) * items_per_page
        _end_index = _start_index + items_per_page

        username = query_params.get('username')
        if username:
            queryset = Video.objects.filter(author__username=username)[_start_index:_end_index]
        else:
            queryset = Video.objects.all()[_start_index:_end_index]
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Video.objects.all()
        teacher = get_object_or_404(queryset, pk=pk)
        serializer = VideoSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TiktokerViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny, ]
    """
    Parameters: items_per_page=10, page=1, username=some_user
    """

    def list(self, request):
        query_params = request.query_params.dict()
        items_per_page = int(query_params.get('items_per_page', '10'))
        page = int(query_params.get('page', '1'))
        _start_index = (page - 1) * items_per_page
        _end_index = _start_index + items_per_page
        username = query_params.get('username')
        if username:
            queryset = Tiktoker.objects.filter(username=username)[_start_index:_end_index]
        else:
            queryset = Tiktoker.objects.all()[_start_index:_end_index]
        serializer = TiktokerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Tiktoker.objects.all()
        tiktoker = get_object_or_404(queryset, pk=pk)
        serializer = TiktokerSerializer(tiktoker)
        return Response(serializer.data, status=status.HTTP_200_OK)
