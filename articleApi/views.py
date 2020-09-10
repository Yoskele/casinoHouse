from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import ArticlePost, Casino, GameSupplier
from .serializers import ArticlePostSerializer, CasinoSerializer, GameSupplierSerializer


class ArticlePostListView(ListAPIView):
    queryset = ArticlePost.objects.order_by('-created_at')
    serializer_class = ArticlePostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


class ArticlePostDetailView(RetrieveAPIView):
    queryset = ArticlePost.objects.order_by('-created_at')
    serializer_class = ArticlePostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


class CasinoListView(ListAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


class CasinoDetailView(RetrieveAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)


class GameSupplierListView(ListAPIView):
    queryset = GameSupplier.objects.all()
    serializer_class = GameSupplierSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )


class GameSupplierDetailView(RetrieveAPIView):
    queryset = GameSupplier.objects.all()
    serializer_class = GameSupplierSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)
