from django.urls import path
from users.views import (
    VideoViewSet,
    TiktokerViewSet
)

urlpatterns = [
    path('videos/', VideoViewSet.as_view({
        'get': 'list',
    })),
    path('videos/<int:pk>/', VideoViewSet.as_view({
        'get': 'retrieve',
    })),
    path('tiktokers/', TiktokerViewSet.as_view({
        'get': 'list',
    })),
    path('tiktokers/<int:pk>/', TiktokerViewSet.as_view({
        'get': 'retrieve',
    })),
]
